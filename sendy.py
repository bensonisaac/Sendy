from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

receivers = ["receiver1@gmail.com", "receiver2@gmail.com"]


sender = "sender@gmail.com"
password = "*********"
receive = ""
subject = "Testing! Check 1, 2"

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <style>
        body {
            font-family: monospace;
        }
        h1 {
            color: blue;
        }
    </style>
    <h1>
        welcome to yournal
    </h1>
    <p>we're happy to have you around.</p>
    <p>Have no fears, start writing today</p>
</body>
</html>
"""

part = MIMEText(html, 'html')


email = MIMEMultipart('alternative')
email["From"] = sender
email["To"] = receive
email["Subject"] = subject
email.attach(part)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    for receive in receivers:
        server.sendmail(sender, receive, email.as_string())