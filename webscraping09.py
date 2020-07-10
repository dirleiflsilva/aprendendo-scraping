"""
parseando arquivo html
navegando nos irmãos
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.next_sibling)
# None

print(soup.td)
# <td class="ce">Tela</td>

print(soup.td.parent)
# <tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>

print(soup.td.next_sibling)
# não imprime nada por que pega o espaço em branco antes da próxima tag!

print(soup.td.next_sibling.next_sibling)
# <td class="cd">Resolução equivalente a tela de 25"</td>

# interando
for sibling in soup.p.next_siblings:
    print(repr(sibling))
"""
'\n'
<h2>Data de lançamento</h2>
'\n'
<p>Donec aliquam urna ut dui placerat porta. Nunc porta, libero nec interdum placerat, neque lacus feugiat tellus, ut iaculis purus nisi eget massa. Sed convallis nisl non nisl posuere fermentum. Cras ac ex convallis, pulvinar nibh at, pharetra sapien. Maecenas fringilla lorem at ante malesuada, et maximus dui pulvinar.</p>
'\n'
<h2>Especificações Técnicas</h2>
'\n'
<table id="tabelaspec">
<caption>Tabela Técnica do Google Glass <span>junho/2016</span></caption>
<tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>
<tr><td class="ce" rowspan="2">Camera</td> <td class="cd"> 5MP para fotos</td></tr>
<tr><td class="cd">720p para vídeos</td></tr>
<tr><td class="ce" rowspan="2">Conectividade</td> <td class="cd">Wi-Fi</td></tr>
<tr><td class="cd">Bluetooth</td></tr>
<tr><td class="ce">Memória Interna</td> <td class="cd">12GB</td></tr>
</table>
'\n'
<h2>Como funciona</h2>
'\n'
<p>Praesent dapibus mattis orci ornare tempus. Sed laoreet accumsan tincidunt. Quisque fermentum dolor nunc. Nullam luctus ultricies sapien, ac facilisis felis commodo a. Duis quis nibh sapien. Sed aliquam felis vel ornare tincidunt.</p>
'\n'
<h2>O que você pode fazer com o Google Glasses</h2>
'\n'
<p>Curabitur tortor mauris, interdum sed tristique at, tincidunt nec justo. Donec rhoncus felis vel tempus faucibus. Sed venenatis consequat ante, sed fermentum ipsum faucibus sit amet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
'\n'
"""

# interando os anteriores
for sibling in soup.p.previous_siblings:
    print(repr(sibling))
""" 
'\n'
<h2>O que é ?</h2>
'\n'
<header id="cabecalho-artigo">
<hgroup>
<h3>Tecnologia &gt;         Inovações</h3>
<h1>Saiba tudo sobre o Google Glass</h1>
<h2>por Thomas William</h2>
</hgroup>
</header>
'\n'
"""