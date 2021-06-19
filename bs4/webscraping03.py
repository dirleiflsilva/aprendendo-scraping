"""
parseando arquivo html / tag
parser padrão
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo01.html','r') as f:
    soup = BeautifulSoup(f,'html.parser')

# busca atributo de p - 1a. ocorrencia!
print(soup.p['class'])

# mostrar atributos de p
print(soup.p.attrs)
# mostrar atributos de a
print(soup.a.attrs)

# acessando atributo - dicionário
print(soup.a['href'])
# acessando atributo - get
print(soup.a.get('href'))

'''
saídas ...
### p
['title']
{'class': ['title']}
### a
{'class': ['sister'], 'href': 'http://example.com/elsie', 'id': 'link1'}
# dicionario
http://example.com/elsie
# get ### mesmo resultado em métodos diferentes!!!
http://example.com/elsie
'''