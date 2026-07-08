from flask import Blueprint, jsonify
from app.store import EVENTS, METRICS

bp = Blueprint("dashboard", __name__, url_prefix="/api")

@bp.get("/dashboard")
def dashboard():
    return jsonify({"metrics": METRICS, "events": EVENTS, "trend": []})
