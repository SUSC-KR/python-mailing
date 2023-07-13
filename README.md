# 단체 이메일 발송 프로그램

## 사용방법

```
.
├── .env
├── README.md
└── main.py

```

1. 구글의 [앱 비밀번호](https://myaccount.google.com/apppasswords?rapt=AEjHL4MXGcHwCfAi78dKXaTl3KrLbVXMSltrDJrH8QcJ4-0AYje5xmidetvsVrrLiRsGK-6f12q2Dg_t9j6dQtAq4rZD8i-vsQ)를 생성한다.
2. gmail 설정에서 IMAP를 활성화한다.
3. 코드로 돌아와 .env 파일을 생성한다.
4. .env 파일에 다음과 같이 작성한다.

```
GOOGLE_ACCOUNT = 구글 아이디
GOOGLE_PASSWORD = 앱 비밀번호
```

5. main.py의 recipients에 보낼 사람들의 이메일들을 추가하고 실행한다.
