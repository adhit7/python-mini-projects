import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Path('index.html').read_text()

email = EmailMessage()
email['from'] = 'Adhi'
email['to'] = 'k3@gmail.com'
email['subject'] = 'Email'


email.set_content(html.substitute({'name':'T'}, 'html'))

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('k4@gmail.com', 'a') #username , password
    smtp.send_message(email)
    print('all done')
