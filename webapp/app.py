from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

@app.route("/add", methods=["POST"])
def add():
    data = request.json.get("data")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO info (data) VALUES (%s);", (data,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "ok"}

@app.route("/get")
def get():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM info;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)
