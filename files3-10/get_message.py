from pprint import pprint

import requests

from settings import token

TOKEN = token
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
pprint(response.json())