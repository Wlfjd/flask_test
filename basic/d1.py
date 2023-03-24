'''
    파이썬 <-> 데이터베이스
    파이썬으로 데이터베이스를 엑세스하여, 쿼리를 전송, 수행결과를 받아오는 방식
        - sql
            - basic에서 수행
            - pymysql 패키지 사용
                - https://github.com/PyMySQL/PyMySQL
        - orm
            - advance에서 수행
    업무 포지션은, 지원팀, 공용 API를 만드는 파트 => 함수, 클래스형태로 라이브러리 제공
    사용방법에 대한 예제까지 제공


    데이터베이스를 터미널 통해서 접속
    1. root 권한으로 mysql 접속하겠다
        $ mysql -u root -p
        Enter password: ********
        MariaDB [(none)]>

    2. 데이터베이스 생성
        create database ml_db;
        Query OK, 1 row affected (0.002 sec)

    3. 데이터베이스 목록 출력 (확인 차)
        show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | ml_db              |
        | mysql              |
        | performance_schema |
        | sys                |
        +--------------------+
        5 rows in set (0.002 sec)


    4. 현재 작업(사용)할 데이터베이스 지정
        use ml_db;
        Database changed
        MariaDB [ml_db]> show tables;

    5. 고객 테이블 생성
    USING BTREE : 검색 속도를 높이는 방식 중에 하나로 특정 컬럼을 지정
    CREATE TABLE `users` 
        (
        `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 관리 ID',
        `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 아이디' COLLATE 'utf8mb4_general_ci',
        `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비번' COLLATE 'utf8mb4_general_ci',
        `name` VARCHAR(30) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci',
        `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일',
        PRIMARY KEY (`id`) USING BTREE,
        UNIQUE INDEX `uid` (`uid`) USING BTREE
    )
    COMMENT='고객 테이블'
    COLLATE='latin1_swedish_ci'
    ENGINE=InnoDB
    ;

    ALTER TABLE `users`

        CHANGE COLUMN `uid` `uid` VARCHAR(32) NOT NULL COLLATE 'latin1_swedish_ci' AFTER `id`,
        CHANGE COLUMN `upw` `upw` VARCHAR(128) NOT NULL COLLATE 'latin1_swedish_ci' AFTER `uid`,
        CHANGE COLUMN `name` `name` VARCHAR(30) NOT NULL COLLATE 'latin1_swedish_ci' AFTER `upw`,
        CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL AFTER `name`;
    SELECT `DEFAULT_COLLATION_NAME` FROM `information_schema`.`SCHEMATA` WHERE `SCHEMA_NAME`='ml_db';


    6. 회원가입 -> insert
        - insert into [<데이터베이스명>.]<테이블명>
            [(컬럼명, 컬럼명, 컬럼명,...)]
        values
            (값, 값, 값,...);
        - 백키 키워드를 테이블명, 컬럼명 등등 사용하면 백틱을 통해 처리 가능
        - '값'
        - now() : mysql의 내장함수로서, 현재시간을 리턴
        -
            INSERT INTO 
                `ml_db`.`users` 
                (`uid`, `upw`, `name`, 'regdate') 
            VALUES 
                ('guest', '1234', '게스트', now());


    8. 회원정보 수정 -> update

    9. 회원탈퇴 -> delete
        - 1년간 보관, 완전 삭제

    7. 로그인 -> select (쿼리의 분량이 가장 많다)
        -- 회원가입 여부 조회 -> 로그인 처리 쿼리
        -- 대소문자 구분 안한다
        -- 제시한 아이디와 비번과 일치하는 row 데이터를 가져와서 uid, name, regdate 값을 조회(출력)하시오
        SELECT
            uid,`name`
        FROM
            users
        WHERE  # 조건
            uid='guest'
        AND 
            upw='1234';

'''
'''
    파이썬에서 DB에 접속, 접속해제
'''
import pymysql as my

connection=None

try:
    # 1. 접속
    connection = my.connect(host='localhost',      # 127.0.01 , 서버 주소
                                #port= 3306             # 포트 , 기본값
                                user='root',           # 사용자 계정, root 계정 외의 계정 사용 권장
                                password='12341234',     # 비밀번호
                                database='ml_db',      # 접속할 데이터베이스
                                #cursorclass=pymysql.cursors.DictCursor)
    )
    print('접속 성공')
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