"""
usando Requests
download imagens
"""
# importando modulo Requests
import requests

url = 'https://st4.depositphotos.com/13349494/21484/i/1600/depositphotos_214848446-stock-photo-delicious-sliced-cheese-rustic-wooden.jpg'
r = requests.get(url)

with open('./teste/imagem.jpg', 'wb') as f:
    f.write(r.content)