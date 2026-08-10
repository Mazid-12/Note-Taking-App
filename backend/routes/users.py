from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from models import create_user

user_bp = Blueprint("users",
                     __name__,
                     url_prefix = "/users")

@user_bp.route("", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    if "username" not in data:
        return {"message": "Username is required"}, 400
    if "password" not in data:
        return {"message": "Password is required"}, 400

    
    username = data["username"]
    password = data["password"]
    password_hash = generate_password_hash(password)

    create_user(username, password_hash )
    return {"message": "user created"}, 201