from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf5a312cd5be0d9d0eff0ee0c6b405510"
# Your Auth Token from twilio.com/console
auth_token  = "a1a8fb1828c541a5ab1b4a79bb63ae05"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Hello my name is Ashrafi!",
    from_="+13347593682",
    to="+919569521145")
print (message.sid)
