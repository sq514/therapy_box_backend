import pymysql;


def connect_to_db():
    return  pymysql.connect(
    host = "therapybox.csefp9hoz2cy.eu-west-2.rds.amazonaws.com",
    port = 3306,
    user = "admin",
    password = "qwertyui",
    db = "TherapyBox"
)

def insert_userInfomation(username,password,email):
    conn = connect_to_db()
    cur=conn.cursor()
    cur.execute("INSERT INTO users (username,password,email) VALUES (%s,%s,%s)", (username,password,email))
    conn.commit()

def select_userInformation(username,password):
    conn = connect_to_db()

    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password=%s",(username,password))
    user = cur.fetchall()
    return user



def insert_userTeam(username,team):
    conn = connect_to_db()
    cur=conn.cursor()
    cur.execute("INSERT INTO user_sport (username,team) VALUES (%s,%s)",(username,team))
    conn.commit()

def update_userTeam(username,team):
    conn = connect_to_db()
    cur=conn.cursor()
    cur.execute("UPDATE user_sport SET team=%s WHERE username=%s",(team,username))
    conn.commit()

def get_userTeam(username):
    conn = connect_to_db()
    cur=conn.cursor() 
    cur.execute("SELECT team FROM user_sport WHERE username = %s",(username))
    team = cur.fetchall()
    return team

def get_userTask(username):
    conn = connect_to_db()
    cur=conn.cursor() 
    cur.execute("SELECT taskID,task,status FROM tasks WHERE username = %s",(username))
    row = [{'id':item[0], 'task':item[1], 'status':item[2]} for item in cur.fetchall()]
    return row

def insert_task(username,task):
    conn = connect_to_db()
    cur=conn.cursor()
    cur.execute("INSERT INTO tasks (username,task,status) VALUES (%s,%s,FALSE)",(username,task))
    conn.commit()

def update_task(taskID,task,status):
    conn = connect_to_db()
    cur=conn.cursor()
    cur.execute("UPDATE tasks SET task=%s,status=%s WHERE taskID=%s",(task,status,taskID))
    conn.commit()