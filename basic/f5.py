'''
    - POST 방식으로 데이터 전송하기

        - 클라이언트 (Json, Xml,Text ,Form(키=값&키=값...), Form-encode, Graphql, Binary)

            - form 전송 =>  화면 껌뻑 후 화면 전환, (Form(키=값&키=값...), Form-encode 형식)
                <form action"http://127.0.0.1:5000/link" methods="post">
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                 </form>
                  ## 이 방식은 사용자가 직접 입력받는 경우에 사용 (가입, 등록, 검색의 형태)

            - ajax 가능 (jQuery로 표현), 화면은 현재 화면 유지
                - (Json, Xml,Text ,Form(키=값&키=값...), Form-encode, Graphql, Binary) 방식 가능
                $.get({
                    url : "http://127.0.0.1:5000/link",
                    data : "name=hello&age=100",
                    success : (res) => {},
                    error: (err) => {}
                })
                ## 무게중심이 클라이언트에 있기 때문에 반드시 응답을 받아야한다
        - 서버
            - post 방식 데이터 추출
            - name= request.form.get('name')
            - age= request.form.get('age')
    
    - /link쪽으로 요청하는 방식은 다양할 수 있다. 단 사이트 설계상 1가지로만 정의되어 있다면 
        다른 방식의 접근은 모두 비정상적인 접근이다 (웹 크롤링, 스크래핑, 해킹 등이 대상)
       이런 접근을 필터링 할 것인가? 보안의 기본사항
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for, session

app = Flask(__name__)
#세션을 위해서 시크릿키 지정
app.secret_key='seserewreadfadf'  # 임의의값, 대부분 해시값 활용

# 로그인을 하여 세션을 얻은 후 홈페이지를 진입해야 사이트 내용을 보여주겠다는 컨셉
@app.route('/')
def home():
    if not 'uid' in session: # 세션에 uid값이 존재하는가?
        # url_for('사용하고자 하는 URL과 연결된 함수명')
        return redirect(url_for('login'))
        # return redirect('login.html')  # url을 사용할 때는 하드코딩하지않는다
    return 'hello world'

# @app.route() => 기본적으로 get방식
# 메소드 추가는 => methods=['POST',...]


@app.route('/login', methods=['POST', 'GET'])
def login():
    # 메소드 별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else:  # post

        # request.form['uid']  => 값이 누락되면 서버 셧다운됨, 사용금지!
 
        # 1. 로그인 정보 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')  # 암호는 차후에 암호화해야한다(관리자도 볼 수 없다, 해싱)
        print(uid, upw)
        # 2. 회원 여부 쿼리
        from d4 import select_login
        result= select_login(uid,upw)
        if result: # 3. 회원이면
            pass
            # 세션 : 클라이언트 정보를 서버가 유지하여서, 간편하게 웹을 이용할 수 있게 도움을 줌
                     # 단점 : 접속 유저가 많으면 서버 측 메모리에 부하가 온다 => 따라서 대안 필요 
                     # JWT를 사용 (사이트 구성 시 인증 쪽으로 활용) 
            # 3-1. 세션생성, 기타 필요한 조치 수행
            session['uid'] = uid  # 키만들고 값
            # 3-2. 서비스 메일 화면으로 이동
            return redirect(url_for('home'))
        else: # 4. 회원아니면
            # 4-1. 적당한 메세지 후 다시 로그인 유도
            # render_template() => jinja2 템플릿 엔진 사용 ==> 문법 jinja2를 따라간다
            return render_template('error.html', msg='로그인 실패')

        #return redirect('https://www.naver.com') # redirect : 요청을 다른 URL로 forwarding한다


if __name__ == '__main__':
    # 웹상에 기본 포트 : http => 80 => 생략 가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True)
