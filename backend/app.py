from database import get_connection
from models import create_user, create_note, get_note, update_note, delete_note, get_user_by_username
from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Note App!"

@app.route("/users", methods=["POST"])
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


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    if "idUser" not in data:
        return {"message": "User ID is required"}, 400
    if "noteContent" not in data:
        return {"message": "Content is required"}, 400
    
    idUser = data['idUser']
    noteContent = data['noteContent']

    create_note(idUser, noteContent)
    return {"message": "note created"}, 201

@app.route("/users/<id_user>/notes", methods=["GET"])
def get_notes(id_user): 
    note_data = get_note(id_user)
    return note_data, 200

@app.route("/notes", methods=["PUT"])
def edit_note():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    if "idNote" not in data:
        return {"message": "Note ID is required"}, 400
    if "noteContent" not in data:
        return {"message": "New content is required"}, 400
    id_note = data['idNote']
    new_content = data['newContent']
    update_note(id_note, new_content)
    return {'message: note updated'}, 200

@app.route('/notes', methods=["DELETE"])
def cancel_note():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 40
    id_note = data['idNote']
    delete_note(id_note)
    return {'message': 'note deleted'}, 200

@app.route('/login', methods=["POST"])
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
    session["user_id"] = user['id']
    return {"message": "Login successful"}, 200


@app.route("/me",  methods=["GET"])
def me():
    user_id = session.get("user_id")
    return {"user_id": user_id}, 200




if __name__=="__main__":
    app.secret_key = "test-secret-key" \
    ""
    app.run(debug=True)
