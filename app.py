from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/') #메인페이지 API
def main():
    return render_template('mainPage.html')

@app.route('/item') #생활용품 API
def item():
    return render_template('itemPage.html')

@app.route('/login') #로그인 API
def login():
    return render_template('loginPage.html')

@app.route('/signup')
def signup():
    return render_template('mainPage.html')
#로그인 페이지


@app.route('/item', methods = ['GET'])
def itemlistLogin(): #로그인시 아이템 리스트 출력
    if request.method == 'GET':
        uid = request.form['id']
        upwd = request.form['pw']
        # session['']


@app.route('/item', methods = ['DELETE'])
def delete(): #선택시 물품 삭제(로그인 되었을 때)
    item_receive = request.form['item_give']
    db.userdb.delete_one({'name':item_receive})
    return jsonify({'alarm' : '삭제 되었습니다.'})

@app.route('/item/List', methods = ['GET'])
def itemListModal(): #아이템 리스트 모달 출력
    item_list = list(db.CYCL.find({},{'_id':False}).sort('number'))
    return jsonify({'item_lists': item_list})

@app.route('/item/Filter', methods = ['GET'])
def itemFilterModal():
    item_kitchen = list(db.CYCL.find({'option':'부엌'},{'_id': False}))
    item
    item_bed = list(db.CYCL.find({'option':'침실'},{'_id' : False}))
    item_bath = list(db.CYCL.find({'option':'화장실'},{'_id' : False}))
    return jsonify({'items_kitchen' : item_kitchen})

@app.route('/item/select',methods = ['GET'])
def itemSelectModal():
    item_receive = request.form['item_give']
    item_list = db.CYCL.find({'name' : item_receive},{'_id': False})
    print(item_list['img'])
    print(item_list['name'])
    print(item_list['timer'])
    return #jsonify({''})

@app.route('/item/add', methods = ['POST'])
def addItemModal(): #모달 아이템을 추가
    user_id_receive = request.form['id_give']
    item_name_receive = request.form['item_name_give']
    start_date_receive = request.form['start_date_give']
    # modal_give로 가져온 값을 가져오면 modal_receive
    print(user_id_receive,item_name_receive,start_date_receive)

    # item_name_receive 값으로 CYCL db에서 해당 name 아이템을 찾아라
    item_name = db.CYCL.find_one({'name' : item_name_receive}, {'_id':False})
    if

    #db.userdb.insert 유저 아이디(user_id), 아이템 이름(item_name), 남은 일자(timer)
    #userdb에.
    item_img = db.CYCL.find_one({'img' : 'item_name')
    item_option = db.CYCL.find_one({'option' : 'item_name'})
    item_
    timer_data =

    db.userdb.insert_one({'uid':'user_id_receive', 'name':'item_name_receive', 'option':'item_option','timer':'timer_data', 'img:item_img'})

    return jsonify({'result':'success', 'select_item':select_item})










    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

