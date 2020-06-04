import smtplib

host = "smtp.gmail.com"
port = 587
username = "modimam1232gmail.com"
password = "pallikutty"
from_mail = username
to_list = ["modimam123@gmail.com"]
try:
    #to establish connection
    email_conn = smtplib.SMTP(host, port)
except:
    print("an error occured")

#to check weather the connection is established or not
email_conn.ehlo()
email_conn.starttls()

try:
    #to log in
    email_conn.login(username, password)
    #to send mail
    email_conn.sendmail(from_mail, to_list, "who are you!!!!")
except:
    print("login failed!!")

#to end connection
email_conn.quit()