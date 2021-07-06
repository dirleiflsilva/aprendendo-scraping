"""
usando Requests
cookies
"""
# importando modulo Requests
import requests

url = 'https://www.google.com.br/'

r = requests.get(url)
#print(r.cookies.get_dict())
cookie = r.cookies.get_dict()

busca = 'web+scraping'
url = 'https://www.google.com/search?q={0}'.format(busca)

r = requests.get(url, cookies=cookie)
#print(r.text)
with open('./teste/google.html', 'w') as f:
    f.write(r.text)

