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
    noteContent = data('noteContent')

    create_note(idUser, noteContent)
    return ("message: note created")

@app.route("/notes", methods=["GET"])
def get_notes():
    data = request.get_json()
    idUser = data['idUser']
    noteData = get_note(idUser)
    return ('message: note found!')
    


if __name__=="__main__":
    app.run(debug=True)
