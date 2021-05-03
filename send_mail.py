import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
MyEmail = "mrsa1380moit@gmail.com"
MyPassword = "mrsa1380"


def send_mail(text, subject, from_email, to_email, html=None):
    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = " , ".join(to_email)
    msg["Subject"] = subject
    text_part = MIMEText(text, "plain")
    msg.attach(text_part)
    if html != None:
        html_part = MIMEText(html, "html")
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(MyEmail, MyPassword)
    server.sendmail(from_email, to_email, msg_str)
    server.quit()
    return "send successfull  😄"


def recognition(username, email, turn):
    html = """\

        <html>
            <head></head>
            <body dir="rtl" style="margin: auto;">
                <h2>Hi {username}<br>
                Welcome to your Sevices 😉 ! <br>
                </h2>
                <h3> Your Turn IS {turn} 😍😇</h3>
            </body>
        </html>

        """.format(username=username, turn=turn)
    send_mail(text=username, subject=turn,
              from_email=MyEmail, to_email=email, html=html)
