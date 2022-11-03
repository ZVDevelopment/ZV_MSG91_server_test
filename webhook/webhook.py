import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"

# data = {'name': 'Zongovita Webhook',
#         'URL': 'TestUrl'}
data = {'name': 'Zongovita Webhook',
        'URL': "api.msg91.com/api/v5/whatsapp/whatsapp-outbound-message/"}


r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})