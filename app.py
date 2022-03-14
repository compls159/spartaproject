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
    return render_template('login sophia.html')

@app.route('/signup') #회원가입페이지 API
def signup():
    return render_template('signUpPage.html')

@app.route('/item', methods = ['GET'])
def itemlistLogin(): #로그인시 아이템 리스트 출력
    if request.method == 'GET':
        uid = request.args.get['id']
        user_item = list(db.userdb.find({'id' : uid},{'_id' : False}))
        return jsonify({'user_item' : user_item})

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
    item_place = request.args.get('place')
    item_lists = list(db.CYCL.find({'option' : item_place}, {'_id' : False}))
    return jsonify({'items_lists' : item_lists})

@app.route('/item/select',methods = ['GET'])
def itemSelectModal():
    item_receive = request.form['item_give']
    item_list = db.CYCL.find({'name' : item_receive},{'_id': False})
    items = [item_list['img'], item_list['name'], item['timer']]
    return jsonify({'items' : items})

@app.route('/item/add', methods = ['POST'])
def addItemModal():

    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
