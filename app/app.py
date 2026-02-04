from flask import Flask, request, make_response
import mysql.connector
from datetime import datetime
import socket

app = Flask(__name__)
SERVER_NAME = socket.gethostname()

def get_db():
    return mysql.connector.connect(
        host="db",      # השם של service ב-docker-compose
        user="root",
        password="root",
        database="appdb"
    )

@app.route("/")
def index():
    db = get_db()
    cur = db.cursor()

    # +1 ל-counter
    cur.execute("UPDATE counter SET value = value + 1 WHERE id=1")
    db.commit()

    # רישום access_log
    client_ip = request.remote_addr
    cur.execute(
        "INSERT INTO access_log (access_time, client_ip, server_ip) VALUES (%s, %s, %s)",
        (datetime.now(), client_ip, SERVER_NAME)
    )
    db.commit()

    # cookie ל-5 דקות
    resp = make_response(SERVER_NAME)
    resp.set_cookie("server_ip", SERVER_NAME, max_age=300)
    return resp

@app.route("/showcount")
def showcount():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT value FROM counter WHERE id=1")
    count = cur.fetchone()[0]
    return str(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
