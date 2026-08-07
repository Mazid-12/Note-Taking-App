import psycopg2
from dotenv import load_dotenv
import os

load_dotenv("../.env")

def get_connection():
    try:
        connector = psycopg2.connect(
            dbname=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port'),
        )

        print('Successful connection')
        connector.close()
        return connector
    except:
        print('Connection failed')

