from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
BACKEND_URL = 'http://18.135.28.88/api'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs', methods=['GET'])
def get_logs():
    response = requests.get(f'{BACKEND_URL}/logs')
    return response.content, response.status_code, response.headers.items()

@app.route('/add_log', methods=['POST'])
def add_log():
    data = request.json
    response = requests.post(f'{BACKEND_URL}/log', json=data)
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)