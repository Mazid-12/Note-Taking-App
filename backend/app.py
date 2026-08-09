from database import get_connection
from models import create_user, create_note, get_note, update_note, delete_note
from flask import Flask, request

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

    create_user(username, password)
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

@app.route("/notes", methods=["GET"])
def get_notes(): 
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
   
    idUser = data['idUser']
    note_data = get_note(idUser)
    return note_data, 201

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
    return {'message: note updated'}, 201

@app.route('/notes', methods=["DELETE"])
def cancel_note():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    id_note = data['idNote']
    delete_note(id_note)
    return {'message': 'note deleted'}, 201


if __name__=="__main__":
    app.run(debug=True)
