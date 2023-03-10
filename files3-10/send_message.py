import requests

from settings import token

TOKEN = token
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {'chat_id': '911336813',
          'text': 'Hello!'}

response = requests.get(url, params)
print(response.json())