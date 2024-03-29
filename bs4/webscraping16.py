"""
usando Requests
"""
# importando modulo Requests
import requests

# URL de busca
url = 'https://www.youtube.com/results?'
payload = {'search_query':'data science academy'}
r = requests.get(url, params = payload)

# retorna todo o código da url
print(r.text)

# retorna apenas a url pesquisada
print(r.url)
# https://www.youtube.com/results?search_query=data+science+academy

print(r.encoding)
# utf-8
