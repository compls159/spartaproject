from flask import Flask, render_template, jsonify, request, session, url_for

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

@app.route("/")
def home():
    if "userID" in session:
        return render_template("signUpPage.html", username=session.get("userID"), login=True)
    else:
        return render_template("signUpPage.html", login=False)

# 회원가입 API
@app.route("/signUp", methods=['POST'])
def signUpCheck():

    # 회원가입을 위한 데이터 받아오기(POST형식)
    id_receive = request.form['id_give'] # 사용자 아이디 값
    pw_receive = request.form['pw_give']  # 사용자 비밀번호 값
    pw2_receive = request.form['pw2_give']  # 사용자 비밀번호 반복입력 값
    name_receive = request.form['name_give']  # 사용자 이름 값
    email_receive = request.form['email_give']  # 사용자 이메일 값

    checkDB = db.Login.find({'user_id': id_receive})['user_id']

    # 조건문 - 클라이언트 폼에서 작성되지 않은 항목 체크
    if id_receive == '' or pw_receive == '' or pw2_receive == '' or name_receive == '' or email_receive == '' :
        return jsonify({'msg': '작성되지 않은 항목이 있습니다'}), url_for("home")
    else:
        # 조건문 - 비밀번호 일치 체크
        if pw_receive != pw2_receive :
            return jsonify({'msg': '비밀번호가 일치하지 않습니다'}), url_for("home")
        else:
            # 조건문 - DB조회 아이디 일치여부
            if id_receive == checkDB :
                return jsonify({'msg': '이미 존재하는 ID입니다'}), url_for("home")
            else:
                # Request 데이터 DB에 추가
                doc = [
                    {
                        'user_id': id_receive,
                        'user_pw': pw_receive,
                        'user_name': name_receive,
                        'user_email': email_receive
                    }
                ]
                db.Login.insert_one(doc)

                # Session 추가
                session['user_id'] = id_receive

                return jsonify({'msg': '회원가입에 성공하였습니다'}), render_template('signUpPage.html', username=session.get('user_id'), login=True)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)