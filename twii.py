#CODE OF SANDEEP N !
from twilio.rest import Client
import requests
import json
account_sid = '---------------------------------------'
auth_token = '----------------------------------------'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
Message = 'Hi '+str(number_iss)
#formulate the message that will be sent
message = client.messages.create(
    to="---------------------",
    from_="------------------",
    body=Message)
print(message.sid)



















