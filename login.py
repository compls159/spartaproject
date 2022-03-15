from flask import Flask, render_template, jsonify, request, session, url_for, redirect

import hashlib

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mc11th

app = Flask(__name__)
app.secret_key="mc11th_key"

@app.route("/")
def home():
    if "user_id" in session:
        return render_template("login_test.html", username=session.get("user_id"), login=True)
    else:
        return render_template("login_test.html", login=False)

# 회원가입 API
@app.route("/login", methods=['GET'])
def login():
	id_receive = request.args.get('login_id')
	pw_receive = hashlib.sha256(request.args.get('login_pw').encode()).hexdigest()

	id_db = db.Login.find({'user_id': id_receive})
	for id in id_db:
		id_db = id['user_id']

	pw_db = db.Login.find({'user_pw': pw_receive})
	for pw in pw_db:
		pw_db = pw['user_pw']

	if id_db == id_receive and pw_db == pw_receive:
		session['user_id'] = id_receive
		return redirect(url_for("home"))
	else:
		return redirect(url_for("home"))

@app.route("/logout")
def logout():
	session.pop('user_id')
	return redirect(url_for("home"))
if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True)