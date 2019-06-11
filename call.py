import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='put-application-id-here',
  private_key='path-to-your-private.key-file',
)

ncco = [
  {
    'action': 'talk',
    'voiceName': 'Salli',
    'text': 'Your message comes here, it\'ll be sent as an automated voice.',
  }
]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': 'country_code_followed_by_number' #eg - 919891234567, don't use +
  }],
  'from': {
    'type': 'phone',
    'number': 'your number registered with nexmo, same format as above.' #eg - 919891234567
  },
  'ncco': ncco
})

pprint(response)