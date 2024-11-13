import os
import psycopg2
from flask import Flask, render_template, Response, request
from datetime import datetime
from db import get_db_connection, init_table_in_db

app = Flask(__name__)


@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    date = datetime.now()
    user_agent = request.headers.get("User-Agent")
    try:
        cur.execute(
            "INSERT INTO counter (date, user_agent) VALUES (%s, %s)", (date, user_agent)
        )
        conn.commit()
    except:
        return Response("{'status':'500'}", status=500, mimetype="application/json")
    cur.close()
    conn.close()
    return {"status": "200"}


@app.route("/count", methods=["GET"])
def get_count():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select count(*) from counter")
    resp = cur.fetchone()
    cur.close()
    conn.close()
    return {"count": resp}


@app.route("/list", methods=["GET"])
def get_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select * from counter;")
    resp = cur.fetchall()
    cur.close()
    conn.close()
    return {"resp": resp}


if __name__ == "__main__":
    init_table_in_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
