from flask import Blueprint, request, session
from models.notes import create_note, get_note, update_note, delete_note, get_one_note


note_bp = Blueprint("note_bp",__name__)

@note_bp.route("/notes", methods=["POST"])
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
    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    if int(current_user_id) != int(idUser):
        return {"error": "Forbidden"}, 403
    
    create_note(idUser, noteContent)
    return {"message": "note created"}, 201


@note_bp.route("/users/<id_user>/notes", methods=["GET"])
def get_notes(id_user): 
    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    if int(current_user_id) != int(id_user):
        return {"error": "Forbidden"}, 403
    note_data = get_note(id_user)
    if note_data is None:
        return {"error": "Note not found"}, 404
    return note_data


@note_bp.route("/users/<id_user>/notes", methods=["PUT"])
def edit_note(id_user):
    data = request.get_json()
    if not data:
        return {"message": "Request body needed"}, 400
    if "idNote" not in data:
        return {"message": "Note ID is required"}, 400
    if "newContent" not in data:
        return {"message": "New content is required"}, 400
    
    id_note = data['idNote']
    new_content = data['newContent']

    note_data = get_one_note(id_note)
    if note_data is None:
        return {"error": "Not found"}, 404
    note_owner_id = note_data["id_user"]
    if int(id_user) != int(note_owner_id):
        return {"error": "Unauthorised"}, 403

    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    if int(current_user_id) != int(id_user):
        return {"error": "Forbidden"}, 403
    
    update_note(id_note, new_content)
    return {'message': 'note updated'}, 200


@note_bp.route('/users/<id_user>/notes/<id_note>', methods=["DELETE"])
def cancel_note(id_user, id_note):
    current_user_id = session.get("user_id")
    if current_user_id == None:
        return {"error": "Not authenticated"}, 401
    if int(current_user_id) != int(id_user):
        return {"error": "Forbidden"}, 403

    note_data = get_one_note(id_note)
    if note_data is None:
        return {"error": "Not found"}, 404
    note_owner_id = note_data["id_user"]
    if int(id_user) != int(note_owner_id):
        return {"error": "Unauthorised"}, 403
    
    delete_note(id_note)
    return {'message': 'note deleted'}, 200