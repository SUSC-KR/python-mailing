# 단체 이메일 발송 프로그램

## 사용방법

```
.
├── README.md
├── bcc-to.csv
├── cc-to.csv
├── content.md
├── main.py
└── send-to.csv

```

1. 구글의 보안 > 2차 인증을 켜고, [앱 비밀번호](https://myaccount.google.com/apppasswords?rapt=AEjHL4MXGcHwCfAi78dKXaTl3KrLbVXMSltrDJrH8QcJ4-0AYje5xmidetvsVrrLiRsGK-6f12q2Dg_t9j6dQtAq4rZD8i-vsQ)를 생성한다.
2. gmail 설정에서 IMAP를 활성화한다.
3. 코드로 돌아와 .env 파일을 생성한다.
4. .env 파일에 다음과 같이 작성한다.

```
GOOGLE_ACCOUNT = "구글 아이디"
GOOGLE_PASSWORD = "앱 2차 비밀번호"
```
5. 아래의 설명에 맞게 파일을 준비해줍니다.
	- 보낼 사람(To): `send-to.csv`
	- 참조 (Cc): `cc-to.csv`
	- 비밀참조(Bcc): `bcc-to.csv`
	``` 
	0
	test0@mail.com
	test1@mail.com
	```

6. `content.md`에 이메일 내용을 작성한다.
7. `subject`를 수정하고 `python main.py`를 실행합니다.
