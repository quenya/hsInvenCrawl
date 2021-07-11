import smtplib
from email.mime.text import MIMEText
import datetime


def send_email():
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()  # TLS 사용시 필요
        id = 'quendya7@gamil.com'
        pw = 'wcqqvwqdfncxzzik'
        smtp.login(id, pw)
        msg = MIMEText('Hs inven crawler started')
        msg['Subject'] = '[%s] Hs inven crawler started' % datetime.datetime.now()
        email = 'qendya@naver.com'
        msg['To'] = email
        smtp.sendmail(id, email, msg.as_string())
        smtp.quit()
    finally:
        print('send mail was failed')


send_email()
