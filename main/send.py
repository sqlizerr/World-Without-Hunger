import requests
import random
import os
from django.contrib.auth.models import User

API = os.environ['API']

def convertTuple(tup):
    str = ''.join(tup)
    return str

def randomemail():
    a= User.objects.values_list('email')
    b= random.choice(a)
    return convertTuple(b)

def send_simple_message(subject, message):
    key = API
    sandbox = 'wldhunger.tk'
    recipient = randomemail()

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