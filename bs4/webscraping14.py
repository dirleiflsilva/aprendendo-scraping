"""
parseando arquivo html
buscando elementos com find_next_sibling/find_previous_sibling
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo03.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

producers = soup.find(id = 'producers')
# busca apenas o 1o. irmão
next_sibling = producers.find_next_sibling()
print(next_sibling)
"""
<ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>
"""

producers = soup.find(id = 'producers')
# busca todos os irmãos
next_siblings = producers.find_next_siblings()
print(next_siblings)
"""
[<ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>, <ul id="secondaryconsumers">
<li class="secondaryconsumerlist">
<div class="name">fox</div>
<div class="number">100</div>
</li>
<li class="secondaryconsumerlist">
<div class="name">bear</div>
				[ 28 ]
				www.it-ebooks.infoChapter 3
				<div class="number">100</div>
</li>
</ul>, <ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>, <ul id="quaternaryconsumers">
<li class="quaternaryconsumerlist">
<div class="name animal">tutle</div>
<div class="number">1000</div>
</li>
<li class="quaternaryconsumerlist">
<div class="name animal">giraffe</div>
<div class="number">100</div>
</li>
</ul>]
"""

producers = soup.find(id = 'quaternaryconsumers')
# busca apenas 1a. irmão anterior
previous_sibling = producers.find_previous_sibling()
print(previous_sibling)
"""
<ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>
"""

producers = soup.find(id = 'quaternaryconsumers')
# busca todos os irmãos anteriores
previous_siblings = producers.find_previous_siblings()
print(previous_siblings)
"""
[<ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>, <ul id="secondaryconsumers">
<li class="secondaryconsumerlist">
<div class="name">fox</div>
<div class="number">100</div>
</li>
<li class="secondaryconsumerlist">
<div class="name">bear</div>
				[ 28 ]
				www.it-ebooks.infoChapter 3
				<div class="number">100</div>
</li>
</ul>, <ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>, <ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>]
"""
