from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/') #메인페이지 API
def main():
    return render_template('main.html')

@app.route('/timerPage') #생활용품 API
def item():
    return render_template('timer.html')

@app.route('/login') #로그인 API
def login():
    return render_template('loginPage.html')

@app.route('/signup') #회원가입페이지 API
def signup():
    return render_template('signUpPage.html')

@app.route('/item', methods = ['GET'])
def itemlistLogin(): #로그인시 아이템 리스트 출력
    if request.method == 'GET':
        uid = request.args.get['id']
        user_item = list(db.userdb.find({'user_id' : uid},{'_id' : False}))
        return jsonify({'user_item' : user_item})

@app.route('/item', methods = ['DELETE'])
def delete(): #선택시 물품 삭제(로그인 되었을 때)
    item_receive = request.form['item_give']
    db.userdb.delete_one({'item_name':item_receive})
    return jsonify({'alarm' : '삭제 되었습니다.'})

@app.route('/item/List', methods = ['GET'])
def itemListModal(): #아이템 리스트 모달 출력
    item_list = list(db.CYCL.find({},{'_id':False}))
    return jsonify({'item_lists': item_list})

@app.route('/item/Filter', methods = ['GET'])
def itemFilterModal():
    item_place = request.args.get('place')
    item_lists = list(db.CYCL.find({'item_place' : item_place}, {'_id' : False}))
    return jsonify({'items_lists' : item_lists})

@app.route('/item/select',methods = ['GET'])
def itemSelectModal():
    item_receive = request.form['item_give']
    item_list = db.CYCL.find({'item_name' : item_receive},{'_id': False})
    items = [item_list['item_img'], item_list['item_name'], item['item_timer']]
    return jsonify({'items' : items})

@app.route('/item/add', methods=['POST'])
def addItemModal():  # 모달 아이템을 추가
    user_id_receive = request.form['id_give']
    item_name_receive = request.form['item_name_give']
    start_date_receive = request.form['start_date_give']
    # ID, 아이템 이름, 주기시작일을 API값으로 받아온다.

    # 아이템 이름으로 찾을 값(name 중복여부, option, timer, img)

    # if 아이템 이름 또는 item name이 없을 때 insert else 있을 때 update
@app.route('/item/add', methods=['POST'])
def addItemModal():  # 모달 아이템을 추가
    user_id_receive = request.form['id_give']
    item_name_receive = request.form['item_name_give']
    start_date_receive = request.form['start_date_give']
    # ID, 아이템 이름, 주기시작일을 API값으로 받아온다.

    # 아이템 이름으로 찾을 값(name 중복여부, option, timer, img)

    # if 아이템 이름 또는 item name이 없을 때 insert else 있을 때 update

    if (db.CYCL.find_one({'id': user_id_receive}, {'_id': False})) == None:
        # uid가 없을 때 insert
        user_id = db.CYCL.find_one({'uid': user_id_receive}, {'_id': False})
        user_name = db.user.find_one({'userName': user_id_receive}, {'_id': False})
        item_name = db.CYCL.find_one({'name': item_name_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'option': item_name_receive}, {'_id': False})
        item_img = db.CYCL.find_one({'img': item_name_receive}, {'_id': False})
        start_date = datetime.datetime(start_date_receive)
        # ↑주기시작일 값을 Timer 기준일로 설정.
        # day = db.CYCL.find_one({'timer':item_name_receive})
        day = item_name['timer']
        # ↑item name 값으로 db에서 추천 주기를 find. 필요 시 나중에 yyyy, m, d로 format 변경
        user_timer = (start_date + day).days
        # ↑userdb에 insert할 user_timer 값 일 단위 계산
        # ↓db.userdb.insert  Uid, 아이템 이름(item_name), 장소(option), 남은 일자(timer), img, startDate
        db.userdb.insert_one(
            {'uid': user_id, 'name': item_name_receive, 'option': item_place, 'timer': user_timer, 'img': item_img,
             'startDate': start_date})
        return jsonify({'result': 'success', 'username': user_name, 'item_name': item_name, 'timer': user_timer})
        # alert ㅇㅇ님 name의 timer가 추가되었습니다.
    elif (db.CYCL.find_one({'id': user_id_receive}, {'_id': False})) != None and (
        db.CYCL.find_one({'name': item_name_receive}, {'_id': False})) == None:
        # uid는 있고 아이템 name은 없을때 insert
        item_name = db.CYCL.find_one({'name': item_name_receive}, {'_id': False})
        user_name = db.user.find_one({'userName': user_id_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'option': item_name_receive}, {'_id': False})
        item_img = db.CYCL.find_one({'img': item_name_receive}, {'_id': False})
        start_date = datetime.datetime(start_date_receive)
        # ↑주기시작일 값을 Timer 기준일로 설정.
        # day = db.CYCL.find_one({'timer':item_name_receive})
        day = item_name['timer']
        # ↑item name 값으로 db에서 추천 주기를 find. 필요 시 나중에 yyyy, m, d로 format 변경
        user_timer = (start_date + day).days
        # ↑userdb에 insert할 user_timer 값 일 단위 계산
        # ↓db.userdb.insert  아이템 이름(item_name), 남은 일자(timer), img
        db.userdb.insert_one({'option': item_place, 'timer': user_timer})
        return jsonify({'result': 'success', 'username': user_name, 'item_name': item_name, 'timer': user_timer})
        # alert ㅇㅇ님 name의 timer가 추가되었습니다.
    elif (db.CYCL.find_one({'id': user_id_receive}, {'_id': False})) != "" and (
        db.CYCL.find_one({'name': item_name_receive}, {'_id': False})) != "":
        # uid도 있고 아이템 name도 있을 때 update
        item_name = db.CYCL.find_one({'name': item_name_receive}, {'_id': False})
        user_name = db.user.find_one({'userName': user_id_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'option': item_name_receive}, {'_id': False})
        item_img = db.CYCL.find_one({'img': item_name_receive}, {'_id': False})
        start_date = datetime.datetime(start_date_receive)
        # ↑주기시작일 값을 Timer 기준일로 설정.
        # day = db.CYCL.find_one({'timer':item_name_receive})
        day = item_name['timer']
        # ↑item name 값으로 db에서 추천 주기를 find. 필요 시 나중에 yyyy, m, d로 format 변경
        user_timer = (start_date + day).days
        # ↑userdb에 insert할 user_timer 값 일 단위 계산
        # ↓db.userdb.insert  아이템 이름(item_name), 남은 일자(timer), img
        db.userdb.update_one({'option': item_place, 'timer': user_timer})
        return jsonify({'result': 'success', 'username': user_name, 'item_name': item_name, 'timer': user_timer})
        # alert ㅇㅇ님 name의 timer가 변경되었습니다.

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
