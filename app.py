from flask import Flask, render_template, jsonify, request
from datetime import datetime
from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/') #메인 페이지 API
def main():
    return render_template('mainPage.html')

@app.route('/item') #생활용품 페이지 API
def item():
    return render_template('itemPage.html')

@app.route('/login') #로그인 페이지 API
def login():
    return render_template('loginPage.html')

@app.route('/signup') #회원가입 페이지 API
def signup():
    return render_template('signUpPage.html')

@app.route('/item/List', methods = ['GET'])
def itemlistLogin(): #로그인 시 아이템 리스트 출력
    if request.method == 'GET':
        uid = request.args.get['id']
        user_item = list(db.UserItem.find({'user_id' : uid},{'_id' : False}))
        return jsonify({'user_item' : user_item})

@app.route('/item/Delete', methods = ['DELETE'])
def delete(): #선택 시 물품 삭제(로그인 되었을 때)
    item_receive = request.form['item_give']
    db.UserItem.delete_one({'item_name':item_receive})
    return jsonify({'alarm' : '삭제 되었습니다.'})

@app.route('/item/modalList', methods = ['GET'])
def itemListModal(): #아이템 리스트 모달 출력
    item_list = list(db.CYCL.find({},{'_id':False}))
    return jsonify({'item_lists': item_list})

@app.route('/item/Place', methods = ['POST'])
def itemFilterPlace():
    item_place_List = request.form('item_place_List')
    item_Place = list(db.CYCL.find({'item_place' : item_place_List}, {'_id' : False}))
    return jsonify({'place_list' : item_Place})

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
    # if user_id이 없거나 user_id와 item_name이 둘 다 없을 때 insert else 둘 다 있을 때 update
    if (db.UserItem.find_one({'user_id': user_id_receive}, {'_id': False})) == None:
        user_id = db.Login.find_one({'user_id': user_id_receive}, {'_id': False})
        user_name = db.Login.find_one({'user_name': user_id_receive}, {'_id': False})
        item_name = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'item_place': item_name_receive}, {'_id': False})
        item_img = db.CYCL.find_one({'item_img': item_name_receive}, {'_id': False})
        start_date = datetime.strptime(start_date_receive)
        # ↑ 주기시작일 값을 Timer 기준일로 설정.
        day = item_name['item_timer']
        # ↑ item_name 값으로 db.CYCL에서 추천 주기를 find. 필요 시 나중에 yyyy, m, d로 format 변경
        item_timer = (start_date + day).days
        # ↑ db.UserItem에 insert할 item_timer 값 일 단위 계산
        # ↓ db.UserItem에 insert user_id, item_name, item_place, item_timer, item_img, start_date
        db.UserItem.insert_one(
            {'user_id': user_id, 'item_name': item_name, 'item_place': item_place, 'item_timer': item_timer, 'item_img': item_img,
             'item_start_Date': start_date})
        return jsonify({'result': 'success', 'user_name': user_name, 'item_name': item_name, 'item_timer': item_timer})
        # alert ㅇㅇ님 item_name의 타이머가 item_timer일 남았습니다.
    elif (db.UserItem.find_one({'user_id': user_id_receive}, {'_id': False})) != None and (
        db.UserItem.find_one({'item_name': item_name_receive}, {'_id': False})) == None:
        user_id = db.Login.find_one({'user_id': user_id_receive}, {'_id': False})
        item_name = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})
        user_name = db.Login.find_one({'user_name': user_id_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'item_place': item_name_receive}, {'_id': False})
        item_img = db.CYCL.find_one({'item_img': item_name_receive}, {'_id': False})
        start_date = datetime.strptime(start_date_receive)
        day = item_name['timer']
        item_timer = (start_date + day).days
        db.UserItem.insert_one(
            {'user_id': user_id, 'item_name': item_name, 'item_place': item_place, 'item_timer': item_timer,
             'item_img': item_img,
             'item_start_Date': start_date})
        return jsonify({'result': 'success', 'user_name': user_name, 'item_name': item_name, 'item_timer': item_timer})
    elif (db.UserItem.find_one({'user_id': user_id_receive}, {'_id': False})) != None and (
        db.UserItem.find_one({'item_name': item_name_receive}, {'_id': False})) != None:
        item_name = db.CYCL.find_one({'item_name': item_name_receive}, {'_id': False})
        user_name = db.Login.find_one({'user_name': user_id_receive}, {'_id': False})
        item_place = db.CYCL.find_one({'item_place': item_name_receive}, {'_id': False})
        start_date = datetime.strptime(start_date_receive)
        day = item_name['timer']
        item_timer = (start_date + day).days
        db.UserItem.update_one({'item_place': item_place, 'item_timer': item_timer, 'item_start_Date': start_date})
        return jsonify({'result': 'success', 'user_name': user_name, 'item_name': item_name, 'item_timer': item_timer})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
