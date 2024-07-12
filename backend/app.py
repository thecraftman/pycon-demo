import os
import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)
DATABASE = 'logs.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                method TEXT NOT NULL,
                status TEXT NOT NULL,
                content_type TEXT
            )
        ''')
        db.commit()        

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    method = data.get('method')
    status = data.get('status')
    content_type = data.get('content_type')
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO logs (method, status) VALUES (?, ?, ?)', (method, status, content_type))
    db.commit()
    return jsonify({"message": "Log entry created"}), 201

@app.route('/logs', methods=['GET']) 
def get_logs():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM logs')
    logs = cursor.fetchall()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)