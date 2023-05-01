"""
usando Requests
"""
import os
# importando modulo Requests
import requests

# Método post
url = 'https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php'
# parametros
payload = {'pagina':'/app/endereco/index.php',
           'endereco':'82510-190',
           'tipoCEP':'ALL'}

response = requests.post(url, data = payload)

# verificar se existe diretorio
if not os.path.exists('./teste'):
    os.makedirs('./teste')

#gravar dados em arquivo
with open('./teste/endereco.html', 'w',encoding = 'utf-8') as f:
    f.write(response.text)
