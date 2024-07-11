import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
  from_addr = 'ie3yyfdimhh3u2z7@ethereal.email'
  login = 'ie3yyfdimhh3u2z7@ethereal.email'
  password = 'xrY8pBz7Twsr5h99Hy'

  msg = MIMEMultipart()
  msg['from'] = 'trip_confirm@email.com'
  msg['to'] = ', '.join(to_addrs)

  msg['Subject'] = 'Trip confirmation'
  msg.attach(MIMEText(body, 'plain'))

  server = smtplib.SMTP('smtp.ethereal.email', 587)
  server.starttls()
  server.login(login, password)
  text = msg.as_string()

  for email in to_addrs:
    server.sendmail(from_addr, email, text)

  server.quit()