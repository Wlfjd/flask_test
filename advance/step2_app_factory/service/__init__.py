from flask import Flask



'''
    create_app은 플라스크 내부에서 정의된 함수명(지정x)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다
    차후, 다른 모듈에서는 flask.current_app이라는 변수로 app을 접근할 수 있다
'''

def create_app():
    app=Flask(__name__)

    @app.route('/')
    def home():
        return "home page 커스텀"

    return app