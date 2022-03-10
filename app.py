from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mc10th

app = Flask(__name__)

# 메인 페이지
@app.route('/main')
def main():
    return render_template('mainPage.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)