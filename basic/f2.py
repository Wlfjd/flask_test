

'''
    라우트 추가 -> URL 추가
'''
from flask import Flask,render_template, jsonify, request, redirect, url_for

app=Flask(__name__)

# 기획서를 기반해서 총 페이지수 만큼 url 준비
# 뼈대를 먼저 잡아서 각 페이지에 해당하는 URL 준비
# 단, blueprint를 사용한다면? 대분류, 중분류(생략가능), 소분류 등 트리구조로 배치한다
# ex) login <-> blueprint 활용 : /auth/users/login
@app.route('/')
def home():
    return 'hello world'

# 아래와 같은 url 구성은 blueprint를 사용하여 섹션을 나눠서 관리하는 것이 더 낫다
@app.route('/auth/users/login')
def login():
    return 'login page'
    
@app.route('/auth/users/signup')
def signup():
    return 'signup page'



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')