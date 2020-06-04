from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


host = "smtp.gmail.com"
port = 587
username = "modimam1232gmail.com"
password = "pallikutty"
from_mail = username
to_list = ["modimam123@gmail.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("alternative")
    the_msg['subject'] = "hello there"
    the_msg['from']= from_mail
    plain_text = "testing the message"
    html_text = """\
        <html>
            <head></head>
            <body>
                <p>hey!<br>
                testing this email <b>message</b>. made by
                <a herf='http://joinfe.com'>team cfe</a>
                </p>
            </body>
        </html>
        """
    part_1 = MIMEText(plain_text, 'text')
    part_2 = MIMEText(html_text, 'html')
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_mail, to_list,the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("error sending message!!!")