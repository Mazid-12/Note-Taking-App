from flask import Blueprint, request, session
from models.notes import create_note, get_note, update_note, delete_note, get_one_note


note_bp = Blueprint("note_bp",__name__)

@note_bp.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    if "noteContent" not in data:
        return {"message": "Content is required"}, 400
    
    idUser = session.get("user_id")
    noteTitle = data["noteTitle"]
    noteContent = data['noteContent']
    
    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    if int(current_user_id) != int(idUser):
        return {"error": "Forbidden"}, 403
    
    create_note(idUser, noteTitle, noteContent)
    return {"message": "note created"}, 201


@note_bp.route("/notes", methods=["GET"])
def get_notes(): 
    current_user_id = session.get("user_id")
    print(current_user_id)
    if current_user_id == None:
        print(current_user_id)
        return {"error": "Not authenticated"}, 401
    note_data = get_note(current_user_id)
    if note_data is None:
        return {"error": "Note not found"}, 404
    return note_data


@note_bp.route("/notes", methods=["PUT"])
def edit_note():
    data = request.get_json()
    current_user_id = session.get("user_id")
    if not data:
        return {"message": "Request body needed"}, 400
    if "idNote" not in data:
        return {"message": "Note ID is required"}, 400
    if "newContent" not in data:
        return {"message": "New content is required"}, 400
    
    id_note = data['idNote']
    new_content = data['newContent']
    new_title = data['newTitle']

    note_data = get_one_note(id_note)
    if note_data is None:
        return {"error": "Not found"}, 404
    note_owner_id = note_data["id_user"]
    if current_user_id != int(note_owner_id):
        return {"error": "Unauthorised"}, 403

    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    
    update_note(id_note, new_title, new_content)
    return {'message': 'note updated'}, 200


@note_bp.route('/notes/<id_note>', methods=["DELETE"])
def cancel_note(id_note):
    print("cacelling")
    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401

    note_data = get_one_note(id_note)
    print(note_data)
    if note_data is None:
        return {"error": "Not found"}, 404
    if note_data["id_user"] != current_user_id:
        return {"error": "Not authorized"}, 403 
    
    delete_note(id_note)
    return {'message': 'note deleted'}, 200