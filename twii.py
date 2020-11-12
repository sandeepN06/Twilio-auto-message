#CODE OF SANDEEP N !
from twilio.rest import Client
import requests
import json
account_sid = 'AC5db2bccf9335d687dba51777f877c0d5'
auth_token = '120fc5d32fc04d6faa804e2677b976df'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
Message = 'Hi '+str(number_iss)
#formulate the message that will be sent
message = client.messages.create(
    to="+917892800801",
    from_="+13158183050",
    body=Message)
print(message.sid)




# importing twilio
# from twilio.rest import Client
#
# # Your Account Sid and Auth Token from twilio.com / console
# account_sid = 'AC5db2bccf9335d687dba51777f877c0d5'
# auth_token = '120fc5d32fc04d6faa804e2677b976df'
#
# client = Client(account_sid, auth_token)
#
# ''' Change the value of 'from' with the number
# received from Twilio and the value of 'to'
# with the number in which you want to send message.'''
# message = client.messages.create(
# 							from_='+13158183050',
# 							body ='body',
# 							to ='+13158183050'
# 						)
#
# print(message.sid)














