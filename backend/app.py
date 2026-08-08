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

    username = data["username"]
    password = data["password"]

    create_user(username, password)
    return ("message: user created")


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()

    idUser = data['idUser']
    noteContent = data['noteContent']

    create_note(idUser, noteContent)
    return ("message: note created")

@app.route("/notes", methods=["GET"])
def get_notes(): 
    data = request.get_json()
    idUser = data['idUser']
    note_data = get_note(idUser)
    return note_data

@app.route("/notes", methods=["PUT"])
def edit_note():
    data = request.get_json()
    id_note = data['idNote']
    new_content = data['newContent']
    update_note(id_note, new_content)
    return ('message: note updated')

@app.route('/notes', methods=["DELETE"])
def cancel_note():
    data = request.get_json()
    id_note = data['idNote']
    delete_note(id_note)
    return ('message: note deleted')


if __name__=="__main__":
    app.run(debug=True)
