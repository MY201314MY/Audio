import json
import requests

print(requests.__version__)

API_KEY = 'nu9r2plGFi3s1ugayDPSM6Mk'
SECRET_KEY = 'G62YGnq84eKTqu0mBgvdpmC6gNBzHdai'

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

print("fetch token begin")
params = {'grant_type': 'client_credentials',
          'client_id': API_KEY,
          'client_secret': SECRET_KEY}

result = requests.get(url=TOKEN_URL, params=params).text
print(result)