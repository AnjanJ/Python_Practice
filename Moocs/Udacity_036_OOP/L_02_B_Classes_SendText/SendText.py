from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACed357f8a74a9d6742124184c5a233343"
auth_token = "80f52506ebfcd30385167123c328844f"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! I love you <3",
  to="+919821991087", # Replace with your phone number
  from_="+19729927151") # Replace with your Twilio number
print message.sid
