'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : url과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request, redirect
from service.controllers import bp_main as main
from service.forms import FormQuestion

@main.route('/') # 플라스크 객체말고 등록한 것도 라우팅 가능
def home():
    return render_template('index.html')

@main.route('/question', methods=['GET','POST']) # 플라스크 객체말고 등록한 것도 라우팅 가능
def question():
    form = FormQuestion()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('main_bp.home'))  # 블루프린트 사용! ~/main
    return render_template('question.html', wtf=form)