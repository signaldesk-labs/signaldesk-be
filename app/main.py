from flask import Flask, jsonify, request
from app.store import EVENTS, METRICS
from app.security import issue_token

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok", "rest_only": True}

    @app.post("/api/auth/login")
    def login():
        payload = request.get_json(silent=True) or {}
        return jsonify({"accessToken": issue_token(payload.get("email", "demo@example.com"))})

    @app.post("/api/auth/refresh")
    def refresh():
        return jsonify({"accessToken": issue_token("refresh-user", "refresh")})

    @app.get("/api/dashboard")
    def dashboard():
        return jsonify({
            "metrics": METRICS,
            "events": EVENTS,
            "trend": [
                {"day": "Mon", "value": 12},
                {"day": "Tue", "value": 18},
                {"day": "Wed", "value": 33},
                {"day": "Thu", "value": 27},
                {"day": "Fri", "value": 41},
            ],
        })

    @app.patch("/api/events/<event_id>/status")
    def update_status(event_id: str):
        payload = request.get_json(silent=True) or {}
        for event in EVENTS:
            if event["id"] == event_id:
                event["status"] = payload.get("status", event["status"])
                return jsonify(event)
        return jsonify({"error": "not_found"}), 404

    return app
