#code is taken from https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest
from twilio.rest import TwilioRestClient

account_sid = "         " # Your Account SID from www.twilio.com/console
auth_token  = "         "  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
your_message_here="Hello User!! Have a great day :) !!"
message = client.messages.create(body=your_message_here,
    to="+91           ",    # Replace with your phone number
    from_="         ")  # Replace with your Twilio number

print(message.sid)
