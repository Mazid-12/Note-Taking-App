from flask import Blueprint, request, session
from models import get_user_by_username
from werkzeug.security import check_password_hash




auth_bp = Blueprint("auth",__name__)

@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = get_user_by_username(username)
    if not user:
        return {"error": "Invalid username or password"}, 401
    is_correct = check_password_hash(user["password"], password)
    if not is_correct:
        return {"error": "Incorrect password"}, 401
    session["user_id"] = user["id"]
    return {"message": "Login successful"}, 200