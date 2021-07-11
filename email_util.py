import smtplib
from email.mime.text import MIMEText
import datetime


def send_email():
    smtp = smtplib.SMTP('smtp.naver.com', 465)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요
    addr = 'lee@live.com'
    pw = '7ujm8i'
    smtp.login(addr, pw)
    msg = MIMEText('Hs inven crawler started')
    msg['Subject'] = '[%s] Hs inven crawler started' % datetime.datetime.now()
    msg['To'] = addr
    smtp.sendmail(addr, addr, msg.as_string())
    smtp.quit()
