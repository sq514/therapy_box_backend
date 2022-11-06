from flask import Flask
from flask import request
from flask_cors import CORS
import json
import db;
app = Flask(__name__)

CORS(app)

@app.route("/api/login", methods=["POST"])
def login():
    body = json.loads(request.data)
    print(body['username'])
    print(body['password'])
    user = db.select_userInformation(body['username'],body['password'])
    if user:
        return {'success':True}
    else:
        return 'information wrong', 401

@app.route("/api/signup", methods=["POST"])
def signUp():
    body = json.loads(request.data)
    db.insert_userInfomation(body['username'],body['password'],body['email'])

    return {'success':True}

@app.route("/api/team", methods=["POST"])
def upsertTeam():
    body = json.loads(request.data)
    if db.get_userTeam(body['username']):
        db.update_userTeam(body['username'],body['team'])
    else:
        db.insert_userTeam(body['username'],body['team'])
    return {'success':True}

@app.route("/api/getteam",methods=["GET"])
def get_team():
    username = request.args.get('username')
    team = db.get_userTeam(username)
    return {"team":team}


@app.route("/api/gettask",methods=['GET'])
def get_task():
    username = request.args.get('username')
    task = db.get_userTask(username)
    print(task)
    return {"task":task}

@app.route("/api/addtask",methods=['POST'])
def add_task():
    body = json.loads(request.data)
    db.insert_task(body['username'],body['task'])
    return {'success':True}
    
@app.route("/api/updatetask",methods=['POST'])
def update_task():
    body = json.loads(request.data)
    db.update_task(body['taskID'],body['task'],body['status'])
    return {'success':True}
