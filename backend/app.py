from flask import Flask
from flask_cors import CORS
from routes.users import user_bp
from routes.auth import auth_bp
from routes.notes import note_bp
from dotenv import load_dotenv
import os

load_dotenv("../.env")

app = Flask(__name__)

CORS(app)

app.secret_key = os.getenv("")
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(note_bp)
app.secret_key = "secret_key"

@app.route("/")
def home():
    return "Welcome to my Note App!"

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_server_error(error):
    return {"error": "Internal server error"}, 500


if __name__=="__main__":
    app.run(debug=False)
