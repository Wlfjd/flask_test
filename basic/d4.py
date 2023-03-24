'''
    데이터 베이스 수행 후 
'''
import pymysql as my

def select_login(uid,upw):
    '''
        아이디, 비밀번호를 넣어서 회우너여부를 체크하는 함수
        parameter
            - uid :아이디
            - upw :비밀번호
        returns
            - 회원인 경우 
                - {'name': '게스트', 'uid': 'guest', 'regdate': datetime.datetime(2023, 3, 24, 13, 2, 31)}
            - 비회원인 경우 or DB측 오류
                - None
    '''
    connection=None
    row=None  # 로그인 쿼리 수행 결과를 담는 변수
    try:
        # 1. 접속
        connection = my.connect(host='localhost',      # 127.0.01 , 서버 주소
                                    #port= 3306             # 포트 , 기본값
                                    user='root',           # 사용자 계정, root 계정 외의 계정 사용 권장
                                    password='12341234',     # 비밀번호
                                    database='ml_db',      # 접속할 데이터베이스
                                    # 조회결과는 [{},{},{},... ] 이런 형태로 추출된다
                                    cursorclass=my.cursors.DictCursor)  # 딕셔너리 커서

        with connection.cursor() as cursor:  # 커서는 with문을 벗어나면 자동으로 닫힘
            # 파라미터는 %s 표시로 순서대로 세팅된다 '값' => ''는 자동으로 세팅된다
            sql= '''
                SELECT
                    `name`, uid, regdate
                FROM
                    users
                WHERE  # 조건
                    uid=%s
                AND 
                    upw=%s;
            '''
            # excute()함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute(sql, (uid,upw))
            row= cursor.fetchone()  # 결과셋 중 한개만 가져온다 -> 단수(리스트가 아닌 단독타입: 딕셔너리)
            # 결과확인 -> 딕셔너리 -> 이름만 추출하시오 -> '게스트'
            # print(row['name'])

            pass
    except Exception as e:
        print('접속 오류',e)

    else:
        print('접속 시 문제 없었음')

    finally:
    # 2. 접속 종료(I/O) -> close()
        if connection:  
            # connection이 참이라면
            connection.close()
    # 로그인한 결과를 리턴 -> {....} 딕셔너리 구조로 리턴
    return row

if __name__ == '__main__':
    # d4 개발자의 테스트 코드
    # f5개발자가 사용할 때는 작동 안함
    # 정상계정
    print(select_login('guest',1234))
    # 비정상계정
    print(select_login('guest',12345))