# Import smtplib for the actual sending function
import smtplib
import sys

# Import the email modules we'll need
from email.mime.text import MIMEText

# メイン関数
if __name__ == '__main__':

    # 以下の内容を変更する
    # me : 自分のGmail アドレス, you : 送信先のアドレス, passwd : Gmailパスワード
    me = sys.argv[1]
    passwd = sys.argv[2]
    you = sys.argv[3]
    titletext = "taitle"
    body = "aa"

    msg = MIMEText(body)
    msg['Subject'] = titletext
    msg['From'] = me
    msg['To'] = you



    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)
    s.send_message(msg)
    s.close()
