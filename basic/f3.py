'''
    클라이언트가 서버에게 데이터를 보내는 방법
    - 방법(method) : GET, POST, PUT,...
         <- http( or https)((HyperText Transfer Protocol) 프로토콜(통신규약, 서로 데이터를 주고받는 약속)에서 정의
         http는 헤더(고정크기) 먼저 전송, 바디(가변크기)를 나중에 전송

         GET 방식 : 헤더만 전송 -> 고정 크기만 전송 => 보낼량이 최대치가 정해져 있다 => 소량만 전송
                    http 헤더만 알면, 패킷(전송데이터)를 가로채서 데이터를 해킹할 수 있다 => 보안취약

         POST 방식 : 헤더(바디 크기가 세팅되어 있음) 전송 후 바디 전송 -> 대량 전송 가능 , 구조를 모르기 때문에 보안에 상대적으로 우수, 암호화 가능 


    - 방식
        - form 전송 : <form> 태그를 사용, 화면이 껌뻑(순식간에 진행), x로 주소창에 아이콘 변경
        - ajax 전송 : 백그라운드로 서버와 통신, 화면은 고정, 껌뻑임 x
        - websocket : 웹소켓을 열어서 통신
        - get 헤더를 활용하여 URL에 데이터를 넣어서 보내는 방식
        - 동적파라미터 : get 의 헤더를 활용하여 URL에 데이터를 넣어서 보내는 방식

    - 동적파라미터
        - http 헤더의 주소 정보를 활용

'''
from flask import Flask,render_template, jsonify, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

# 동적파라미터, 문자열타입으로 전송
# 용량은 헤더 사이즈, 주소 크기를 초과할 수 없다
# 파라미터는 함수 인자를 통해서 함수 내부로 진입
# #,<,> 은 전달 안됨/ 한글, 특수, 영대, 영소 다 가능
#  URL 인코딩으로 전달하면 모두 전달 가능
@app.route('/news/<news_id>')
def news(news_id):
    return '전달된 데이터[%s]' % news_id



# 1개 이상도 전달 가능한가?, 위치조정
# http://127.0.0.1:5000/전달값1/news2/전달값2
# 결론 ===> # URL을 무한대로 생산할 수 있다
@app.route('/<news_id>/news2/<news_author>')
def news2(news_id, news_author):
    return '전달된 데이터[%s][%s]' % (news_id, news_author)

# 타입 제한이 가능한가? int, float, path
# http://127.0.0.1:5000/news3/전달값2/ 12345678  -> 202 OK
# http://127.0.0.1:5000/news3/전달값2/ hello     -> 404 OK  

@app.route('/news3/<int:news_id>')
def news3(news_id):
    return '전달된 데이터[%s]' % news_id


# path
# 전달값을 무한대로 늘려주는 옵션 = news4이하로는 무한대로 가능
# http://127.0.0.1:5000/news4/1/2/3/4/5/6/7/8/9/동국/10
@app.route('/news4/<path:news_id>')
def news4(news_id):
    return '전달된 데이터[%s]' % news_id

if __name__ == '__main__':
    # 웹상에 기본 포트 : http => 80 => 생략 가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, port=5000, host='0.0.0.0')