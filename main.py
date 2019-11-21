import socket
from email.mime.text import MIMEText

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('google.com', 80))
msg = MIMEText("Here is the body of my message")
msg["From"] = "admin@orangehrm.com"
msg["To"] = "chanaka@orangehrmlive.com"
msg["Subject"] = "This is the asd subject."
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_string())

if result == 0:
   print "Port is open"
else:
   print "Port is not open"