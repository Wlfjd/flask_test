#  파이썬 기반 웹 프로그래밍

# 목표
    - 단계
        - 기획
        - 스토리보드
        - 디자인 시안, 데이터베이스 모델링, 빠르게 프로토타입 만듬(끝까지 가본다)
        - 분야별 
            - 프런트
                - 디자인 진행(페이지 단위 계산), html 코딩, 스크립트 처리
                - React or Vue or Angular : 전면, 부분 구성
            - 백엔드
                - 기능별 구현
                - 페이지별 진행 -> url을 준비한다는 뜻 ! 만약 10개라면 
                - 모델 서빙, 머신러닝(딥러닝 관련) 서비스 기능 삽입
                - 데이터 분석, 시각화 -> 파이썬 기반 웹에서 가지는 강점(파이썬으로 구성되기 때문)
            - 공통 기능 구현
            - 통신 프로토콜 구현
                - 요청과 응답 정리
            - 데이터베이스
                - DB 설계
                - 테이블 구성
                - 쿼리 구성
    - 웹 환경 이해 및 웹 프로그램 구성 이해
    - flask 기반 웹기반 백엔드(서버) 프로그래밍
    - blueprint를 이용한 기능별 분할구성(=업무 나눠서 작업 가능)
        - 회원관련 업무(가입, 로그인, 로그아웃, 탈퇴, 세션관리, 쿠키,..) : A 개발자 담당
        - 모델 서빙 파트 (데이터 전처리, 모델 예측수행, 응답처리,..) : B 개발자 담당
        - 데이터베이스 관련 업무(SQL or ORM 준비, API 준비, 데이터베이스 준비) : C 개발자 담당(DBA 업무 포함)
    - 데이터베이스 연동(sql, ORM,..)
    - 배포 및 운영
        - 실제 회사, 개발팀 개발 완료 => 전달 => 운영팀이 세팅 운영/유지보수 진행

# 발전적 목표
    - 머신러닝(딥러닝 포함) 모델 서빙 및 서비스를 구현
    - 구축된 서비스를 도커 및 쿠버네티스 기반하에서 운영
    - MLOps 연동사용


# 가상환경 구축
    - 순수 파이썬
        - 가상환경을 모아두는 폴더 생성
            - mkdir venus
        - 해당 폴더로 이동
            - cd venvs
        - 가상환경 생성
            - python -m venv 가상환경이름
            - python -m venv web
        - 가상환경 활성화하는 명령어 위치까지 이동
            - cd ./web/Scripts
        - 가상환경 활성화
            - activatenb(맥, 리눅스)
            or
            - . activate(윈도윈)
        - 최종 프럼프트 형태
            - (web) >  : 윈도우
            - (web) $  : 맥/리눅스 사용자 계정
            - (web) #  : 맥/리눅스 루트 계정

    - 아나콘다(미니콘다, ..)

# 필요한 패키지 설치
    - requirements.txt 생성
    - 작성
        - 수동
            - 직접 기압
            - 패키지 == 버전
            - 패키지
        - 자동 : 
            - 개발이 다 종료된 후, 개발중에 생성한다면
                - 패키지가 이미 일부 설치가 혹은 전부 설치가 되어있다
                - 내가 설치하지 않은 패키지도 추가된다
            - pip freeze > requirementst.txt

    - 설치
        - pip install -r requirements.txt  
    
    - 번외
        - pip를 수행하면 command와 option 안내가 나와 다양한 기능 소개
        - ex) 
            - pip show pandas
                - WARNING: Package(s) not found: pandas
                -> 해당 패키지가 설치되어 있다면 노출, 없다면 경고