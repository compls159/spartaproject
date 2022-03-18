from flask import Flask, render_template, jsonify, request, session, redirect, url_for, flash
from pymongo import MongoClient

from datetime import datetime, timedelta

import hashlib

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc11th

app = Flask(__name__)
app.secret_key = "mc11th_key"


# 메인 페이지
@app.route('/')  # 메인 페이지 API
def main():
    if "user_id" in session:
        return render_template('mainPage.html', login=True)
    else:
        return render_template('mainPage.html', login=False)


@app.route('/item')  # 생활용품 페이지 API
def item():
    if "user_id" in session:
        return render_template('itemPage.html', username=session.get("user_id"), login=True)
    else:
        return render_template('itemPage.html', login=False)


@app.route('/login')  # 로그인 페이지 API
def login():
    if "user_id" in session:
        return render_template("loginPage.html", username=session.get("user_id"), login=True)
    else:
        return render_template("loginPage.html", login=False)


@app.route('/signUp')  # 회원가입 페이지 API
def signUp():
    if "user_id" in session:
        return render_template("signUpPage.html", username=session.get("user_id"), login=True)
    else:
        return render_template("signUpPage.html", login=False)


# 로그인 API
@app.route("/login/chk", methods=['GET'])
def loginCheck():
    id_receive = request.args.get('login_id')
    pw_receive = request.args.get('login_pw')
    print(id_receive, pw_receive)
    if pw_receive is None:
        flash('아이디 및 비밀번호를 입력해주세요')
        return redirect(url_for("login"))
    else:
        pw_receive = hashlib.sha256(request.args.get('login_pw').encode()).hexdigest()

        id_db = db.Login.find({'user_id': id_receive})
        for id in id_db:
            id_db = id['user_id']

        pw_db = db.Login.find({'user_pw': pw_receive})
        for pw in pw_db:
            pw_db = pw['user_pw']

        if id_db == id_receive and pw_db == pw_receive:
            session['user_id'] = id_receive
            flash('로그인에 성공하였습니다')
            return redirect(url_for("login"))
        else:
            flash('로그인에 실패하였습니다')
            return redirect(url_for("login"))


@app.route("/login/logout")
def logout():
    session.pop('user_id')
    return redirect(url_for("login"))


# 회원가입 API
@app.route("/signUp/chk", methods=['GET'])
def signUpCheck():
    # 회원가입을 위한 데이터 받아오기(POST형식)
    id_receive = request.args.get('signUpId')  # 사용자 아이디 값
    pw_receive = hashlib.sha256(request.args.get('signUpPw').encode()).hexdigest()  # 사용자 비밀번호 값을 sha256을 사용해 encrypt
    pw2_receive = hashlib.sha256(
        request.args.get('signUpPw2').encode()).hexdigest()  # 사용자 비밀번호 일치값을 sha256을 사용해 encrypt
    name_receive = request.args.get('signUpName')  # 사용자 이름 값
    email_receive = request.args.get('signUpEmail')  # 사용자 이메일 값

    checkDB = db.Login.find({'user_id': id_receive})
    for chk in checkDB:
        checkDB = chk['user_id']

    # 조건문 - 클라이언트 폼에서 작성되지 않은 항목 체크
    if id_receive == '' or pw_receive == '' or pw2_receive == '' or name_receive == '' or email_receive == '':
        flash('작성되지 않은 항목이 있습니다')
        return redirect(url_for("signUp"))
    else:
        # 조건문 - 비밀번호 일치 체크
        if pw_receive != pw2_receive:
            flash('비밀번호가 일치하지 않습니다')
            return redirect(url_for("signUp"))
        else:
            # 조건문 - DB조회 아이디 일치여부
            if id_receive == checkDB:
                flash('이미 존재하는 ID입니다')
                return redirect(url_for("signUp"))
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
                db.Login.insert_many(doc)
                # Session 추가
                session['user_id'] = id_receive
                flash('회원가입 완료되었습니다. 감사합니다')
                return redirect(url_for("signUp"))


@app.route('/item/List', methods=['GET'])
def itemlistLogin():  # 로그인 시 아이템 리스트 출력
    if request.method == 'GET':
        uid = request.args.get('username')
        print(uid)
        user_item = list(db.UserItem.find({'user_id': uid}, {'_id': False}))
        return jsonify({'user_item': user_item})


@app.route('/item/Delete', methods=['DELETE'])
def delete():  # 선택 시 물품 삭제(로그인 되었을 때)
    item_receive = request.form['item_give']
    db.UserItem.delete_one({'item_name': item_receive})
    return jsonify({'alarm': '삭제 되었습니다.'})


# if 장소 없으면 modalList , #if 장소 있으면 filter
@app.route('/item/modalList', methods=['GET'])
def itemListModal():  # 아이템 리스트 모달 출력
    item_list = list(db.CYCL.find({}, {'_id': False}))
    return jsonify({'item_lists': item_list})


@app.route('/item/Place', methods=['GET'])
def itemFilterPlace():
    item_Place = list(db.CYCL.find({}, {'_id': False}))
    return jsonify({'all_place': item_Place})


@app.route('/item/Filter', methods=['GET'])
def itemFilterModal():
    item_place = request.args.get('place')
    item_lists = list(db.CYCL.find({'item_place': item_place}, {'_id': False}))
    return jsonify({'items_lists': item_lists})


@app.route('/item/select', methods=['GET'])
def itemSelectModal():
    item_receive = request.form['item_give']
    item_list = db.CYCL.find({'item_name': item_receive}, {'_id': False})
    items = [item_list['item_img'], item_list['item_name'], item['item_timer']]
    return jsonify({'items': items})


@app.route('/item/add', methods=['POST'])
def addItemModal():  # 모달 아이템을 추가

    # 값을 받아옴 - 유저아이디, 상품 이름, 주기 시작일
    global id_receive
    id_receive = request.form['id_give']
    global name_receive
    name_receive = request.form['item_name_give']
    global date_receive
    date_receive = request.form['start_date_give']

    # 값을 가져옴 - 상품 주기 - None Type 정의 필요
    global timer
    timer = db.CYCL.find_one({'item_name': name_receive}, {'_id': False})

    if timer == "":
        timer = 0
    else:
        timer = timer['item_timer']

    # 주기 시작일에 상품 주기를 더해 디데이 생성
    date_change = datetime.strptime(date_receive, "%Y-%m-%d")
    day_plus = timedelta(days=timer)
    date_end = date_change + day_plus
    date_end = str(date_end).split(' ')[0]
    print(date_end)

    # 조회 DB 변수 설정
    global chkId
    chkId = db.UserItem.find_one({'user_id': id_receive}, {'_id': False})
    if chkId == "":
        chkId = ""
        return chkId

    else:
        chkId = chkId['user_id']
        chkName = db.UserItem.find_one({'item_name': name_receive}, {'_id': False})
    if chkName == "":
        chkName = ""
        return chkName
    else:
        chkName = chkName['item_name']


    # 조건 1 - 아이템 DB에 유저 아이디 조회, 없다면 변수  설정, 아이템 추가
    if chkId == "" and chkName == "":
        return jsonify({'msg': '해당하는 아이템이 존재하지 않습니다.'})
        item_place = db.CYCL.find_one({'item_name': name_receive})
        item_place = item_place["item_place"]

        item_timer = db.CYCL.find_one({'item_name': name_receive})["item_place"]
        item_timer = item_timer['item_timer']

        item_img = db.CYCL.find_one({'item_name': name_receive})["item_img"]
        item_img = item_img['item_img']
    doc = [
        {'user_id': id_receive,
         'item_name': name_receive,
         'item_place': item_place,
         'item_timer': item_timer,
         'item_startDate': date_receive,
         'item_endDate': date_end
         }]
    return jsonify({'userItem': doc})


# 조건 2 - 아이템 DB에 유저 아이디 조회, 없다면 상품 이름 조회, 있다면 아이템 추가
    if chkId == "" and chkName == "":
        doc = [
            {'user_id': id_receive,
             'item_name': name_receive,
             'item_place': item_place,
             'item_timer': item_timer,
             'item_startDate': date_receive,
             'item_endDate': date_end
             }]
        # return jsonify({'userItem': doc})

    # 조건 3 - 아이템 DB에 유저 아이디 조회, 있다면 상품 이름 조회, 있다면 시작일 업데이트
    if chkId != "" and chkName != "":
        db.UserItem.update_one({"item_name": name_receive}, {"$set": {"item_startDate": date_receive}})
    # return jsonify({'msg': '저장되었습니다.'})

# 아이디가 있고 아이템 이름이 없는 경우
# elif idDB != None and nameDB == None:
#     # user_id = db.Login.find_one({'user_id': user_id_receive}, {'_id': False})
#     item_name = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})
#     item_place = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})["item_place"]
#     item_img = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})["item_img"]
#     start_date = start_date_receive
#     day = item_name['timer']
#     item_timer = (start_date + day).days
#     doc = [
#         {'user_id': user_id_receive,
#          'item_name': item_name,
#          'item_place': item_place,
#          'item_timer': item_timer,
#          'item_img': item_img,
#          'item_start_Date': start_date_receive}
#     ]
#     db.UserItem.insert_many(doc)
#     return jsonify({'result': 'success'})
#
# # 아이디가 있고 아이템 이름도 있는 경우
# elif idDB != None and nameDB != None:
#     # item_name = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})
#     # item_place = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})["item_place"]
#     # start_date = start_date_receive
#     # day = item_name['timer']
#     # item_timer = (start_date + day).days
#     # doc = [
#     #     {'item_place': item_place,
#     #      'item_timer': item_timer,
#     #      'item_start_Date': start_date}
#     # ]
#     db.UserItem.update_one(
#         {'item_name' : item_name_receive},{"$set":{ "item_startDate": start_date_receive}}
#     )
#
#     return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
