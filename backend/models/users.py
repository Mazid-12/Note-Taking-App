from database import get_connection

def create_user(username, password_hash):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"insert into users (username, password_hash) values ('{username}', '{password_hash}');"
    cursor.execute(query)
    print('user created!')
    connector.commit()
    connector.close()

def get_user_by_username(username):
    connector = get_connection()
    cursor = connector.cursor()
    query = f"select * from users where username = '{username}';"
    cursor.execute(query)
    user_data = cursor.fetchone()
    connector.commit()
    connector.close()
    if not user_data:
        return {}
    user = {}
    user["id"]= user_data[0]
    user["username"]= user_data[1]
    user["password"]= user_data[2]
    return user