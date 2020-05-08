from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo01.html','r') as f:
    soup = BeautifulSoup(f,'html.parser')

print(soup.p['class'])

print(soup.p.attrs)

# acessando atributo - dicionário
print(soup.a['href'])

# acessando atributo - get
print(soup.a.get('href'))
