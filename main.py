import os
import smtplib
import re
import markdown
import pandas as pd

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class EmailSender:
    def __init__(self, smtp_server, smtp_port, account, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.account = account
        self.password = password
        self.smtp = None

    def connect(self):
        self.smtp = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        self.smtp.login(self.account, self.password)

    def disconnect(self):
        if self.smtp:
            self.smtp.quit()

    def send_email(self, recipients, subject, cc, content):
        for recipient in recipients:

            message = MIMEMultipart()
            message["Subject"] = subject
            message["From"] = self.account
            message["To"] = recipient

            if cc:
                message["Cc"] = cc

            with open(content, 'r') as file:
                markdown_content = file.read()
                html_content = markdown.markdown(markdown_content)

            content_part = MIMEText(html_content, "html")
            message.attach(content_part)

            try:
                self.smtp.sendmail(self.account, recipient, message.as_string())
                print(f"정상적으로 메일이 발송되었습니다: {recipient}")
            except Exception as e:
                print(f"메일 발송 중 오류가 발생했습니다: {recipient} - {str(e)}")


load_dotenv()
smtp_server = "smtp.gmail.com"
smtp_port = 465
account = os.getenv('GOOGLE_ACCOUNT')
password = os.getenv('GOOGLE_PASSWORD')
sender = EmailSender(smtp_server, smtp_port, account, password)

participants = pd.read_csv("./parti.csv")
participants = participants['0']

recipients = list(participants) ## 보낼 사람들의 이메일 리스트 입력
subject = "Test Mail"
cc = os.getenv('CC_MAIL') ## 참조할 사람들의 이메일 리스트 입력
content = "content.md"

sender.connect()
sender.send_email(recipients, subject, cc,  content)
sender.disconnect()
