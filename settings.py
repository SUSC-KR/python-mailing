import os

from dotenv import load_dotenv
load_dotenv()

MAIL_TITLE = "SUSC Winter OT 티켓 안내 및 CS101 스터디 모집"
MAIL_BODY_PATH = 'content.md'

DATA_PATH = './susc-winter-dataset.csv'
EMAIL_LABEL = '이메일 주소'

SMTP_PORT = 465
ACCOUNT = os.getenv('GOOGLE_ACCOUNT')
PASSWORD = os.getenv('GOOGLE_PASSWORD')

SEND_TO_PATH = './send-to.csv'
CCS_PATH = './cc-to.csv'
BCCS_PATH = './bcc-to.csv'