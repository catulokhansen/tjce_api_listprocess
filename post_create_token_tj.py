import requests
from pprint import pprint

# URL API TJ-CE to generate access token (the token expires in 30 minutes after creation)
url = 'https://consultaprocesso.tjce.jus.br/scpu-web/api/kdjklsajdls/jsldaskd'

# User and Password for API authentication
user_data = {
"nomeUsuario": "PGM",
"senha": "WnZObjFmZlFYMXB4YWg="
}

# Send verb HTTP POST with parameters for access token generation 
response = requests.post(url=url, json=user_data)

# Success or Error essage return 
if response.status_code >= 200 and response.status_code <= 299:
    # Sucess
    print(response.status_code)
    print(response.reason)
    print(response.text)
   
     
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)

# Variables to store API returno in json
response_data = response.json()
token = response_data['token']

# Write the returned token to to file
with open(r'tj_api\'token.txt', 'w') as file:
        file.write(token)
   
