'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : url과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request,url_for, jsonify
from service.controllers import bp_auth as auth
# 시간정보 획득하는 함수와 시간차를 계산하는 함수
from datetime import datetime, timedelta
# Flask 객체 획득
from flask import current_app
import jwt
import bcrypt

@auth.route('/') # 플라스크 객체말고 등록한 것도 라우팅 가능
def home():
    # url_for("별칭.함수명") => url이 리턴된다
    #print(url_for('auth_bp.login'))
    return "auth 홈"

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # jwt 관련체크 => 정상(200), 오류(401)
        # 1. uid,upw 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 2. uid,upw로 회원이 존재하는지 체크 -> (원래디비,임시로 값 비교)
        if uid=='guest' and upw=='1234':
        # 3. 회원이면 토큰 생성 (규격, 만료시간, 암호알고리즘 구성, ...)
            payload= {
                 # 페이로드는 데이터 자체를 의미, json 형태
                 # 저장할 정보는 알아서 구성(고객정보 기반)
                    'id':uid,
                    
                    # 만료시간(원하는대로 설정)
                    # 토큰이 발급되고 나서 + 24시간 후에 토큰은 만료된다
                    'exp': datetime.utcnow()+timedelta(seconds=60*60*24)
            }
            # 토큰발급 => 시크릿키, 해시알고리즘("HS256"), 데이터(payload)
            SECRET_KEY = current_app.config['SECRET_KEY']  # 환경변수 값 획득

            # 발급
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')  #구글은 HS256알고리즘만 지원한다
            print(token)
            # 4. 응답 전문 구성 -> 응답
            return jsonify( {'code':1, 'token':token} )

    

@auth.route('/logout') # 플라스크 객체말고 등록한 것도 라우팅 가능
def logout():
    return "auth logout"

@auth.route('/signup') # 플라스크 객체말고 등록한 것도 라우팅 가능
def signup():
    # TODO: 비밀번호 암호화
    password='1234'
    # 암호화된 값은 디비에 패스워드 컬럼에 저장
    b= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # 확인 및 복호화
    # bcrypt.checkpw() => 이것으로 암호가 일치하는지만 체크해서 로그인 시 활용
    print(password,b,bcrypt.checkpw(password.encode('utf-8'),b))
    return "auth signup"

@auth.route('/delete') # 플라스크 객체말고 등록한 것도 라우팅 가능
def delete():
    return "auth delete"