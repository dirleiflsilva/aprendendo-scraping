"""
parseando arquivo html
navegando pelas tags
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

# sempre vai buscar a 1a. ocorrência!
print(soup.title)
# <title>Tudo Sobre Google Glass</title>

print(soup.head.title)
# <title>Tudo Sobre Google Glass</title>

print(soup.a)
# <a href="https://www.facebook.com/TheLifelongTeacher/?fref=ts" target="_blank">Facebook</a>

print(soup.a.img)
# None

print(soup.td)
# <td class="ce">Tela</td>

print(soup.tr)
# <tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>

print(soup.tr.td)
# <td class="ce">Tela</td>

print(soup.td.attrs) # atributo
# {'class': ['ce']}

print(soup.td['class'])
# ['ce']

print(soup.td['class'][0])
# ce
