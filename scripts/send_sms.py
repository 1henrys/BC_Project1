# Download the helper library from https://www.twilio.com/docs/python/install
# pip install twilio
import os
import dotenv
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_msg(msgbody, to_number):
    dotenv.load_dotenv()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                    body=msgbody,
                    from_='+14084405432', # Don't change this number.
                    to=to_number #'+15512088818'  # This number has to be a twilio verified number
                 )

    return message.sid

msgbody = "Join Earth's mightiest heroes. Like Kevin Bacon."
to_number = '+15512088818'
msid = send_msg(msgbody, to_number)
print(msid)