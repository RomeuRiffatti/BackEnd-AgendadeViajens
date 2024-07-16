import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(to_addrs, body):
    from_addr = "oavffp5igbfvvx6z@ethereal.email" 
    login = "oavffp5igbfvvx6z@ethereal.email"
    password = "CJganCyP5dWVnS696U"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = 'romeufftt@gmail.com'.join(to_addrs)

    msg["Subject"] = "Confirmaçao de viajem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)

    server.starttls()
    server.login(login,password)
    text = msg.as_string()
    
    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()
