from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def sendemail(fromAddress, toAddress, subject, message):
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())

