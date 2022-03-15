from flask import Flask, render_template, jsonify, request, session, redirect, url_for

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)
app.secret_key="webSecret@123"

ID = "hello"
PW = "world"

@app.route("/")
def home():
    if "userID" in session:
        return render_template("login_test.html", username = session.get("userID"), login=True)
    else:
        return render_template("login_test.html", login=False)

@app.route("/login", methods=["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and _password_ == PW:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)