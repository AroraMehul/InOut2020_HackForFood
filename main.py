from flask import Flask, jsonify, request, Response
import json
import requests
from flask_cors import CORS
from login import login, signup
from pool import create_pool, join_pool

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/auth/login', methods=['GET', 'POST'])
def login_():
	data = request.json
	out = login(data['email'], data['password'])
	return jsonify(
			status=out
		)

@app.route('/auth/signup', methods=['GET', 'POST'])
def signup_():
	data = request.json
	out = signup(data['email'], data['password'])
	return jsonify(
			status=out
		)

@app.route('/pool/create', methods=['GET', 'POST'])
def create():
	data= request.json
	out = create_pool(data['p1'], data['subscript'], data['startDate'], data['duration'])
	return jsonify(
			status=out
		)

@app.route('/pool/join', methods=['GET', 'POST'])
def join():
	data= request.json
	out = join_pool(data['uid'], data['p1'])
	return jsonify(
			status=out
		)

if __name__ == '__main__':
    app.run()