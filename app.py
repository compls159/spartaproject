from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/main') #메인페이지 API
def main():
    return render_template('mainPage.html')

@app.route('/main') #생활용품 API
def item():
    return render_template('itemPage.html')

@app.route('/main') #로그인 API
def login():
    return render_template('loginPage.html')

#로그인 페이지
@app.route('/login') #메인페이지 API
def main():
    return render_template('mainPage.html')

@app.route('/login') #회원가입페이저 API
def signup():
    return render_template('signUpPage.html')

#회원가입 페이지
@app.route('/signup') #메인페이지API
def signup():
    return render_template('mainPage.html')

#생활용품페이지
@app.route('/life') #메인페이지API
def main():
    return render_template('mainPage.html')

@app.route('/life') #이용방법API
def goitem():
    return render_template('itemPage.html')

@app.route('/life')
def gologin():
    return render_template('loginPage.html')

@app.route('/life', methods = ['GET'])
def itemlist():
    return

@app.route('/life', methods = ['DELETE'])
def delete():
    return

@app.route('/life', methods = ['GET'])
def itemListModal():
    return

@app.route('/life', methods = ['GET'])
def itemFilterModal():
    return

@app.route('/life',methods = ['GET'])
def itemSelectModal():
    return

@app.route('/life', methods = ['POST'])
def addItemModal():
    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
