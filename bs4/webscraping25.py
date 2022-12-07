"""
usando Requests
session Object
"""
# importando modulo Requests
import requests

url = 'https://www.google.com.br/'

s = requests.Session()
s.get(url)
#print(r.cookies.get_dict())
cookie = s.cookies.get_dict()
#print(cookie)

busca = 'web+scraping'
url = 'https://www.google.com/search?q={0}'.format(busca)

r = s.get(url)
#print(r.text)
with open('./teste/google-sessionObject.html', 'w') as f:
    f.write(r.text)

