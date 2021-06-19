"""
parseando arquivo html
navegando pelos filhos
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.table.contents)
"""
['\n', <caption>Tabela Técnica do Google Glass <span>junho/2016</span></caption>, 
 '\n', <tr><td class="ce">Tela</td> 
           <td class="cd">Resolução equivalente a tela de 25"</td>
       </tr>,
 '\n', <tr><td class="ce" rowspan="2">Camera</td> 
           <td class="cd"> 5MP para fotos</td>
       </tr>,
 '\n', <tr><td class="cd">720p para vídeos</td></tr>,
 '\n', <tr><td class="ce" rowspan="2">Conectividade</td> 
           <td class="cd">Wi-Fi</td>
       </tr>, 
 '\n', <tr><td class="cd">Bluetooth</td></tr>, 
 '\n', <tr><td class="ce">Memória Interna</td> 
           <td class="cd">12GB</td>
       </tr>,
 '\n']
"""
print(type(soup.table.contents))
# <class 'list'>

print(len(soup.table.contents))
# 15

print(soup.table.contents[1])
# <caption>Tabela Técnica do Google Glass <span>junho/2016</span></caption>

print(soup.table.contents[1].span)
# <span>junho/2016</span>

print(soup.table.contents[1].span.string)
# junho/2016

print(soup.table.contents[3])
# <tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>

print(soup.table.contents[3].td)
# <td class="ce">Tela</td>

# interando nos filhos (lista)
for child in soup.table.contents:
    if child.name == 'tr':
        print(child)
"""
<tr><td class="ce">Tela</td> <td class="cd">Resolução equivalente a tela de 25"</td></tr>
<tr><td class="ce" rowspan="2">Camera</td> <td class="cd"> 5MP para fotos</td></tr>
<tr><td class="cd">720p para vídeos</td></tr>
<tr><td class="ce" rowspan="2">Conectividade</td> <td class="cd">Wi-Fi</td></tr>
<tr><td class="cd">Bluetooth</td></tr>
<tr><td class="ce">Memória Interna</td> <td class="cd">12GB</td></tr>
"""
print(type(soup.children))
# <class 'list_iterator'>

for child in soup.footer.children:
    print(child)
"""
<p>Copyright © 2013 - by Thomas William <br/>
<a href="https://www.facebook.com/TheLifelongTeacher/?fref=ts" target="_blank">Facebook</a> | 
	<a href="https://www.udemy.com/user/marcoscastrodesouza/" target="_blank">Udemy</a></p>
"""
### contents / children = acessam apenas filhos diretos, não descendentes!

for child in soup.footer.p.children:
    if child.name == 'a':
        print(child.get('href'))
"""
https://www.facebook.com/TheLifelongTeacher/?fref=ts
https://www.udemy.com/user/marcoscastrodesouza/
"""

# filhos diretos
print(len(list(soup.children)))
# 2

# filhos descendentes
print(len(list(soup.descendants)))
# 164