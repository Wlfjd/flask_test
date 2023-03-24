import pymysql as my

connection=None

try:
    # 1. 접속
    connection = my.connect(host='localhost',      # 127.0.01 , 서버 주소
                                #port= 3306             # 포트 , 기본값
                                user='root',           # 사용자 계정, root 계정 외의 계정 사용 권장
                                password='12341234',     # 비밀번호
                                database='ml_db',      # 접속할 데이터베이스
                                # 조회결과는 [{},{},{},... ] 이런 형태로 추출된다
                                cursorclass=my.cursors.DictCursor)  # 딕셔너리 커서
    )
    

    with connection.cursor() as cursor:  # 커서는 with문을 벗어나면 자동으로 닫힘
   
        sql= '''
            SELECT
                uid,`name`
            FROM
                users
            WHERE  # 조건
                uid='guest'
            AND 
                upw='1234';
        '''
        cursor.execute(sql)
        row= cursor.fetchone()  
        # 결과확인 -> 딕셔너리 -> 이름만 추출하시오 -> '게스트'
        print(row['name'])

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
    print('접속종료 성공')