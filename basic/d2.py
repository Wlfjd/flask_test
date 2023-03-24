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
                                # 만약 사용 안하면 [(),(),(),..] 이런 형태로 나옴
                                # cursorclass=my.cursors.DictCursor)
    )
    
    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다 ( Rule에 따라 )
    # 1. 커서 획득
    with connection.cursor() as cursor:
        # spq문 준비
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
        # 3. sql 쿼리 수행
        cursor.execute(sql)

        # 4. 결과를 획득
        row= cursor.fetchone()  # 결과가 한개로 나오니까 row

        # 5. 결과 확인 -> 이름만 추출하시오 -> 순서가 중요, 인덱싱
        #    튜플로 결과를 받는 것은 결과값의 순서가 바뀌지 않는 전제하에 가능
        #    순서없는 자료구조 : 딕셔너리!! => d3
        print(row[1])

        
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