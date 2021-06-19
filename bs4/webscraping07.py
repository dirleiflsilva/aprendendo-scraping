"""
parseando arquivo html
navegando pelos filhos diretos / descendentes
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

# abrir arquivo para leitura
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

#for tag in soup.descendants: ### para facilitar vamos trabalhar apenas com a tag <footer>
for tag in soup.footer.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)
# footer do arquivo html
"""
<p>Copyright © 2013 - by Thomas William <br/>
<a href="https://www.facebook.com/TheLifelongTeacher/?fref=ts" target="_blank">Facebook</a> | 
	<a href="https://www.udemy.com/user/marcoscastrodesouza/" target="_blank">Udemy</a></p>
"""
# retorno soup.footer.descendants
"""
p
Copyright © 2013 - by Thomas William 
br
a
Facebook
 | 

a
Udemy
"""

for tag in soup.footer.descendants:
    if isinstance(tag, Tag):
        print(tag)
"""
<p>Copyright © 2013 - by Thomas William <br/>
<a href="https://www.facebook.com/TheLifelongTeacher/?fref=ts" target="_blank">Facebook</a> | 
	<a href="https://www.udemy.com/user/marcoscastrodesouza/" target="_blank">Udemy</a></p>
<br/>
<a href="https://www.facebook.com/TheLifelongTeacher/?fref=ts" target="_blank">Facebook</a>
<a href="https://www.udemy.com/user/marcoscastrodesouza/" target="_blank">Udemy</a>
"""

# diferença entre strings e stripped_strings
for string in soup.aside.strings:
    print(repr(string))
"""
'\n'
'Outras Notícias'
'\n'
'Vídeo mais recente'
'\n'
'\n'
'\n'
'\n'
'\n\t\tDesculpe, mas não foi possível carregar o vídeo\n\t'
'\n'
'Novidades'
'\n'
'Phasellus fermentum non diam vitae ultricies. Aliquam fermentum justo eget venenatis luctus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam orci lectus, molestie non elit nec, tincidunt suscipit nisi. Morbi libero mauris, sodales eu massa eget. \n\n\tPellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent id fringilla arcu. Cras nec massa ex. Integer maximus facilisis congue. Suspendisse potenti. Nunc molestie arcu a elementum ultricies.'
'\n'
"""

for string in soup.aside.stripped_strings:
    print(repr(string))
"""
'Outras Notícias'
'Vídeo mais recente'
'Desculpe, mas não foi possível carregar o vídeo'
'Novidades'
'Phasellus fermentum non diam vitae ultricies. Aliquam fermentum justo eget venenatis luctus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam orci lectus, molestie non elit nec, tincidunt suscipit nisi. Morbi libero mauris, sodales eu massa eget. \n\n\tPellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent id fringilla arcu. Cras nec massa ex. Integer maximus facilisis congue. Suspendisse potenti. Nunc molestie arcu a elementum ultricies.'
"""
