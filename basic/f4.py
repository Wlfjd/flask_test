'''
    - GET 방식으로데이터 전송하기

        - 클라이언트 (키=값&키=값...)
            - 링크 => 화면 전화
                <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
                ## 상세보기에 적절(게시판)

            - form 전송 =>  화면 껌뻑 후 화면 전환
                <form action"http://127.0.0.1:5000/link" methods="get">
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                 </form>
                  ## 이 방식은 사용자가 직접 입력받는 경우에 사용 (가입, 등록, 검색의 형태)

            - ajax 가능 (jQuery로 표현)
                $.get({
                    url : "http://127.0.0.1:5000/link",
                    data : "name=hello&age=100",
                    success : (res) => {},
                    error: (err) => {}
                })
                ## 무게중심이 클라이언트에 있기 때문에 반드시 응답을 받아야한다
        - 서버
            - get 방식 데이터 추출
            - name= request.args.get('name')
            - age= request.args.get('age')
    
    - /link쪽으로 요청하는 방식은 다양할 수 있다. 단 사이트 설계상 1가지로만 정의되어 있다면 
        다른 방식의 접근은 모두 비정상적인 접근이다 (웹 크롤링, 스크래핑, 해킹 등이 대상)
       이런 접근을 필터링 할 것인가? 보안의 기본사항
'''
from flask import Flask,render_template, jsonify, request, redirect, url_for

app=Flask(__name__)

@app.route('/link')
def link():
    # request.args['age'] => 데이터 누락시 서버 셧다운 됨, 사용하면 안됨
    # request.args.get('age') => 데이터 누락시 None이 나와서 예외처리 가능함
    name= request.args.get('name')  
    age= request.args.get('age')
    return "[%s][%s]" % (name,age)


@app.route('/test')
def test():
    # 엔트리포인트(진입로, 프로그램 시작)과 같은 경로에 templates/test.html 생성
    return render_template('test.html')


if __name__ == '__main__':
    # 웹상에 기본 포트 : http => 80 => 생략 가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, port=5000, host='0.0.0.0')