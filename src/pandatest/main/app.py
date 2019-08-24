import pandas as pd
import numpy as np
import requests
import json

url = "https://free-nba.p.rapidapi.com/games"
headers = {'Content-Type': 'application/json',
           # 'Authorization': 'Bearer {0}'.format(api_token)
           'x-rapidapi-key': '5b1ab052e0mshe7071b7fd347de5p13df3cjsn626953fb4523'
           }

response = requests.get(url, headers=headers)
print(response.status_code)
json_response = response.json()
for counter in range(5):
    print(json_response['data'][counter]['home_team']['city'])
