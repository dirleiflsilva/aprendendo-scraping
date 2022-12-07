"""
usando Requests
timeout
"""
# importando modulo Requests
import requests

#response = requests.get('http://www.google.com', timeout = 10)
#response = requests.get('http://www.google.com', timeout = 0.01)
#response = requests.get('http://www.google.com', timeout = None)
# tempo retorno, tempo leitura
response = requests.get('http://www.google.com', timeout = (0.2, 0.2))
print(response.url)
