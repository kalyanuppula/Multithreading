#hvdg fawf hyik gdjk
import smtplib
import threading

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_email():
    otp = random.randint(1111,9999)

    body = f"""
            <html>
                <body>
                    <h1 style="background-color:black;height:30px;color:white;padding:10px;margin:10px;">OTP For Verification - {otp}</h1>
                </body>
            </html>
            """
    msg = MIMEMultipart()
    msg["From"] = "saivardhan.thimmisetty@gmail.com"
    msg["To"] = "saivardhan2408@gmail.com"
    msg["Subject"] = "OTP - University Management System"
    msg.attach(MIMEText(body,"html"))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("saivardhan.thimmisetty@gmail.com","caon tcoy rldi uktj")
    server.send_message(msg)
    server.quit()
    msg = MIMEMultipart()
print("Sending.....")
t = threading.Thread(target=send_email)
t.start()
print("Sent......")
