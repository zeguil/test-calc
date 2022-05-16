from twilio.rest import Client
from telesign.messaging import MessagingClient
from telesign.phoneid import PhoneIdClient

def send_sms_twilio(code):
    account_sid = ''
    auth_token = ''
    message = f"Seu código de verificação: {code}"
    server_number = "+19706140300"
    client_number = ""

    client = Client(account_sid, auth_token)
    client.messages.create(from_=server_number,body=message, to=jhon)


def send_sms_telesign(code):
    customer_id = ""
    api_key = ""
    phone_number = "55"+""
    message = f"Seu código de verificação: {code}"
    message_type = "ARN"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)


def send_wpp(code):
    account_sid = ''
    auth_token = ''
    server_number = ""
    client_number = ""
    message = f"Seu código de verificação: {code}"

    client = Client(account_sid, auth_token)
    client.messages.create(from_=server_number,body=message,to=client_number)


