from flask import Flask
from flask import request
from flask_cors import CORS
import json
app = Flask(__name__)

CORS(app)

@app.route("/api/login", methods=["POST"])
def login():
    body = json.loads(request.data)
    print(body['username'])
    print(body['password'])
    
    return body