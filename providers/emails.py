import os, sys, smtplib, logging as log
from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import re

def validEmail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True

def render_template(template, token, name):
    p = Path(__file__).parent.parent/'satic'/'templates'
    templateLoader = FileSystemLoader(searchpath=Path(p))
    templateEnv = Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)

    data = {'token':token, 'name':name.title()}
    return templ.render(data)

def send_email(email, token, name):

    html = render_template('email.j2', token=token, name=name)

    # UMBLER VARS
    HOST_SMTP_UMBLER = "smtp.umbler.com"
    PORT_UMBLER = 587
    EMAIL_UMBLER = "contato@guilhermelins.dev.br"
    SENHA_UMBLER = os.environ['SENHA_UMBLER']

    #Entrando no servidor
    server = smtplib.SMTP(HOST_SMTP_UMBLER, PORT_UMBLER)
    server.starttls() # alguns casos
    server.login(EMAIL_UMBLER, SENHA_UMBLER)


    # Montando email
    message = MIMEMultipart()
    message['From'] = EMAIL_UMBLER
    message['To'] = email
    message['Subject'] = '[Autoponia] Redifinição de senha'
    message.attach(MIMEText(html, 'html'))

    try:
        # Enviar email
        log.info(f'sending email to {email}')
        server.sendmail(message['From'], message['To'], message.as_string())
    except Exception as e:
        log.error('Error sending email')
        log.exception(str(e))
    finally:
        # Fechar servidor
        server.quit()



#fastapi-mail
#https://sabuhish.github.io/fastapi-mail/getting-started/