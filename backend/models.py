from database import get_connection

#CREATE
def create_user(username, password_hash):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"insert into users (username, password_hash) values ('{username}', '{password_hash}');"
        cursor.execute(query)
        print('user created!')
        cursor.close()
        connector.close()
    except:
        print('user not created')

def create_note(id_user, content):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"insert into notes (id_user, content) values ({id_user}, {content});"
        cursor.execute(query)
        cursor.close()
        connector.close()
        print('note created')
    except:
        print('note not created')

#READ
def get_note(id_user):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"select * from notes where id_user = '{id_user}';"
        cursor.execute(query)
        notes = cursor.fetchall()
        notes_list = []
        for note in notes:
            note_dict = {
                'idUser': note[1],
                'idNote': note[0],
                'content': note[2]
            }
            notes_list.append(note_dict)
        return notes_list
        cursor.close()
        connector.close()
    except:
        print('no not found')

#UPDATE
def update_note(id_note, new_content):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"update notes set content = '{new_content}' where id_note = '{id_note}';"
        cursor.execute(query)
        print('note updated sucessfully!')
        cursor.close()
        connector.close()
    except:
        print('update failed!')

#DELETE
def delete_note(id_note):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"delete from notes where id_note = '{id_note}';"
        cursor.execute(query)
        print('note deleted sucessfully!')
        cursor.close()
        connector.close()
    except:
        print('deletion failed!')
