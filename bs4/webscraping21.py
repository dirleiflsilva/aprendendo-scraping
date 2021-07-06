"""
usando Requests
redirecionamento (response)
"""
# importando modulo Requests
import requests

url = 'http://webplatform.org'

response = requests.get(url)
print(response.url)
#https://webplatform.github.io/
print(response.history)
#[<Response [301]>]
print(response.status_code)
#200
print(response.history[0].status_code)
#301
print(response.history[0].headers)
#{'content-length': '0', 'location': 'https://webplatform.github.io/'}
print(response.history[0].headers['Location'])
#https://webplatform.github.io/

# não quero redirecionamento
r = requests.get('http://webplatform.org', allow_redirects = False)
print(r.url)
#https://webplatform.org/
print(r.history)
#[]
