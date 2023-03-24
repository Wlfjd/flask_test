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

import pymysql as my