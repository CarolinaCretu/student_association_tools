from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
import pandas as pd

path = input("path: ")
df = pd.read_csv(path)

email_sender = 'nextgenbiotech.fabit@gmail.com'
email_password = input('password: ')
email_receivers = list(df.Email)

subject = 'Trying automated emails'


def send_email(receivers):
    for person in receivers:
        my_email = MIMEMultipart()
        my_email['From'] = email_sender
        my_email['To'] = person
        my_email['Subject'] = subject
        html = """
        <html>
            <body>
                <center>
                    <h1>title</h1>
                        <p> This is the first paragraph.</p>
                        <p> This is the second paragraph.</p>
                </center>

            </body>
        </html>
        """
        my_email.attach(MIMEText(html, "html"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, person, my_email.as_string())


send_email(email_receivers)

