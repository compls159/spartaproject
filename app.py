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

@app.route('/timerPage') #생활용품 API
def item():
    return render_template('timer.html')

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
def delete(): #선택시 물품 삭제
    item_receive = request.form['item_give']
    db.CYCL.delete_one({'name':item_receive})
    return jsonify({'alarm' : '삭제 되었습니다.'})

@app.route('/item', methods = ['GET'])
def itemListModal(): #아이템 리스트 모달 출력
    item_list = list(db.CYCL.find({},{'_id':False}).sort('number'))
    return jsonify({'item_lists': item_list})

@app.route('/item', methods = ['GET'])
def itemFilterModal():
    item_kitchen = list(db.CYCL.find({'option':'부엌'},{'_id': False}))
    item
    item_bed = list(db.CYCL.find({'option':'침실'},{'_id' : False}))
    item_bath = list(db.CYCL.find({'option':'화장실'},{'_id' : False}))
    return jsonify({'items_kitchen' : item_kitchen})

@app.route('/item',methods = ['GET'])
def itemSelectModal():
    item_receive = request.form['item_give']
    item_list = db.CYCL.find({'name' : item_receive},{'_id': False})
    print(item_list['img'])
    print(item_list['name'])
    print(item_list['timer'])
    return #jsonify({''})

@app.route('/item', methods = ['POST'])
def addItemModal():

    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

