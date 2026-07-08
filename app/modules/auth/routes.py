from flask import Blueprint, jsonify, request
from app.security import issue_token

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    return jsonify({"accessToken": issue_token(payload.get("email", "demo@example.com"))})
