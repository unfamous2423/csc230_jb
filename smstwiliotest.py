from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console

account_sid = 'ACe362bd3848430949363c937b2748df9e'

auth_token = '' \
             '61014b3112c2d075e7b9659ade35fd0e'

client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Wow this is a robo text. It's time for the DOWNTOWN DUNKARONI THREE CHEESE BRONCO DICK SURPRISE WONDERMIN'S HELLSHIT FROM OUTER SPACE YOU BITCH",
                     from_='+14437477203',
                     to='+14432069068'
                 )

print(message.sid)