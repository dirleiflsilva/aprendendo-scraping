"""
usando Requests
"""
# importando modulo Requests
import requests

# Método post
url = 'https://context.reverso.net'
# parametros
payload = {'search':'"pesquisa',
           'source_lang':'en',
           'target_lang':'pt'}

response = requests.post(url, data = payload)
#gravar dados em arquivo
with open('./teste/reverso.html', 'w',encoding = 'utf-8') as f:
    f.write(response.text)
