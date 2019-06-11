import nexmo

client = nexmo.Client(key='your-key', secret='your-secret') #you'll get these from Nexmo

client.send_message({
    'from': 'Nexmo',
    'to': '919891234567', #receiver's number, country-code followed by number, don't use +
    'text': 'Message to be sent.',
})
