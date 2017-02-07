import smtplib
from email.mime.text import MIMEText


class EmailService():
    def __init__(self, user, password):
        self._from = user
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(user, password)

    def __exit__(self):
        self.server.close()

    def send(self, to, subject, content):
        msg = MIMEText(content)
        msg["From"] = self._from
        msg["To"] = to
        msg["Subject"] = subject

        self.server.send_message(msg)


service = EmailService("codeorgok@gmail.com", "Codecool2016!")

service.send("codeorgok@gmail.com", "teszt email", "teszt uzenet")
