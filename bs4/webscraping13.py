"""
parseando arquivo html
buscando elementos com find_parent / find_parents
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo04.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

primaryconsumers = soup.find_all(class_ = 'primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
#print(primaryconsumer)

parent_ul = primaryconsumer.find_parent('ul')
print(parent_ul)
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
parent_ul = primaryconsumer.find_parents('ul')
print(parent_ul)
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
</ul>, <ul id="parent_producers">
<li class="parent_producerlist">
<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>
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
<ul id="secondaryconsumers">
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
</ul>
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
<ul id="quaternaryconsumers">
<li class="quaternaryconsumerlist">
<div class="name animal">tutle</div>
<div class="number">1000</div>
</li>
<li class="quaternaryconsumerlist">
<div class="name animal">giraffe</div>
<div class="number">100</div>
</li>
</ul>
</li>
</ul>]
"""