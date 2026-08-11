from database import get_connection

def create_note(id_user, content):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"insert into notes (id_user, content) values ('{id_user}', '{content}');"
    cursor.execute(query)
    connector.commit()
    connector.close()

    print('note created')



def get_note(id_user):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"select * from notes where id_user = '{id_user}';"
    cursor.execute(query)
    notes = cursor.fetchall()
    notes_list = []
    note_dict = {}
    if not notes:
        return None
    for note in notes:
        note_dict['idUser'] =note[1]
        note_dict['idNote'] = note[0]
        note_dict['content'] = note[2]
        notes_list.append(note_dict)
        note_dict = {}
    print(notes_list)
    connector.commit()
    connector.close()
    return notes_list

def get_one_note(id_note):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"select id_user, content from notes where id_notes = '{id_note}';"
    cursor.execute(query)
    notes = cursor.fetchone()
    if not notes:
        return None
    note_dict = {}
    note_dict["id_user"] = notes[0]
    note_dict["content"] = notes[1]
    connector.commit()
    connector.close()
    return note_dict

def update_note(id_note, new_content):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"update notes set content = '{new_content}' where id_notes = '{id_note}';"
    cursor.execute(query)
    print('note updated sucessfully!')
    connector.commit()
    connector.close()


def delete_note(id_note):
    try:
        connector = get_connection()
        cursor = connector.cursor()
        query = f"delete from notes where id_notes = '{id_note}';"
        cursor.execute(query)
        print('note deleted sucessfully!')
        connector.commit()
        connector.close()
    except:
        print('deletion failed!')
