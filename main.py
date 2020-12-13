from flask import Flask, jsonify, request, Response
import json
import requests
from flask_cors import CORS
from login import login, signup
from pool import create_pool, join_pool
from wallet import add_money, check_balance, deduct_money
from cookiemanager import create_cookie, fetch_cookie

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/auth/login', methods=['GET', 'POST'])
def login_():
	data = request.json
	out, user = login(data['email'], data['password'])
	return jsonify(
			status=out,
			res=user
		)

@app.route('/auth/signup', methods=['GET', 'POST'])
def signup_():
	data = request.json
	print(data)
	out, user = signup(data['name'], data['email'], data['password'])
	return jsonify(
			status=out,
			res=user
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


@app.route('/wallet/addMoney', methods=['POST'])
def addMoney():
	data= request.json
	out = add_money(data['uid'], data['amt'])
	return jsonify(
			status=out
		)

@app.route('/wallet/checkBal', methods=['POST'])
def checkBal():
	data= request.json
	out = check_balance(data['uid'])
	status = 1
	if(out == -2) : status = -2 
	return jsonify(
			status= status,
			res = out
		)

@app.route('/wallet/deductMoney', methods=['POST'])
def deductMoney():
	data= request.json
	out = deduct_money(data['uid'], data['amt'])
	return jsonify(
			status=out
		)

@app.route('/cook/create_cookie', methods=['POST'])
def createCookie():
	data= request.json
	out = deduct_money(data['uid'], data['besan'])
	return jsonify(
			status=out
		)

@app.route('/cook/fetch_cookie', methods=['POST'])
def fetchCookie():
	data = request.json
	out = deduct_money(data['uid'])
	status = 1
	if(out == -2) : 
		status = -2
		out  = ""
	return jsonify(
			status=status,
			res = json.loads(out)
		)

if __name__ == '__main__':
    app.run()