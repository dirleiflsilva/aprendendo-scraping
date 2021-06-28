"""
parseando arquivo html
navegando nos pais
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.parent)
# None ### tag atual <html> não tem pai

tag_title = soup.title
print(tag_title)
# <title>Tudo Sobre Google Glass</title>

print(tag_title.parent)
"""
<head>
<title>Tudo Sobre Google Glass</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
</head>
"""

print(soup.td)
# <td class="ce">Tela</td>

print(soup.td.parent)
# <tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>

print(soup.td.parent.parent) # acessando avó
"""
<table id="tabelaspec">
<caption>Tabela Técnica do Google Glass <span>junho/2016</span></caption>
<tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>
<tr><td class="ce" rowspan="2">Camera</td> <td class="cd"> 5MP para fotos</td></tr>
<tr><td class="cd">720p para vídeos</td></tr>
<tr><td class="ce" rowspan="2">Conectividade</td> <td class="cd">Wi-Fi</td></tr>
<tr><td class="cd">Bluetooth</td></tr>
<tr><td class="ce">Memória Interna</td> <td class="cd">12GB</td></tr>
</table>
"""

for pai in soup.p.parents:
    print(pai.name)
"""
article
section
div
body
html
[document]
"""
