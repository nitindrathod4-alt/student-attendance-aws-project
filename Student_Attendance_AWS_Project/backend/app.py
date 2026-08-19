from flask import Flask, jsonify
import os
import mysql.connector

app=Flask(__name__)

def db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST","<RDS_ENDPOINT>"),
        user=os.getenv("DB_USER","admin"),
        password=os.getenv("DB_PASSWORD","CHANGE_ME"),
        database=os.getenv("DB_NAME","studentdb")
    )

@app.get("/")
def home():
    return jsonify({"message":"Student Management API is running","server":os.uname().nodename})

@app.get("/api/students")
def students():
    conn=db()
    cur=conn.cursor(dictionary=True)
    cur.execute("SELECT name, roll_no, attendance, result FROM students ORDER BY roll_no")
    data=cur.fetchall()
    cur.close(); conn.close()
    return jsonify(data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)
