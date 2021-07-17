import requests
import os

API = os.environ['API']

def send_message(subject, message):
    key = API
    sandbox = 'wldhunger.tk'
    recipient = "vedangreserve@gmail.com"

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'admin@wldhunger.tk',
        'to': recipient,
        'subject': subject,
        'text': message
    })

    print ('Status: {0}'.format(request.status_code))
    print ('Body:   {0}'.format(request.text))
    print (recipient)
    print ("Someone has contacted you")