from bs4 import BeautifulSoup

with open('arquivo01.html','r') as f:
    soup = BeautifulSoup(f, 'html5lib')

# transforma em uma string bem formatada
#print(soup.prettify())

# retorna texto de todas as tags
#print(soup.get_text())

# buscando texto de uma tag específica
#print(soup.p.get_text())

# buscando texto da tag atual
#print(soup.p.string)
print(soup.p.b.string)


