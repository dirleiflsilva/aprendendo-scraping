"""
parseando arquivo html
navegando entre os elementos
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup
from bs4.element import Tag

# abrir arquivo para leitura
with open('arquivo03.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

#         <div> \n           <ul>
print(soup.div.next_element.next_element)

#<ul id="producers">
#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>
#<li class="producerlist">
#<div class="name">algae</div>
#<div class="number">100000</div>
#</li>
#</ul>

#         div> \n           <ul>         \n           <li>
print(soup.div.next_element.next_element.next_element.next_element)

#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>

# retornando ...
#        <li> \n              <ul>
print(soup.li.previous_element.previous_element)

#<ul id="producers">
#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>
#<li class="producerlist">
#<div class="name">algae</div>
#<div class="number">100000</div>
#</li>
#</ul>

# importar bs4.element
for e in soup.ul.next_elements:
    if isinstance(e, Tag):
        print(e)

#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>
#<div class="name">plants</div>
#<div class="number">100000</div>
#<li class="producerlist">
#<div class="name">algae</div>
#<div class="number">100000</div>
#</li>
#<div class="name">algae</div>
#<div class="number">100000</div>
#<ul id="primaryconsumers">
#<li class="primaryconsumerlist">
#<div class="name">deer</div>
#<div class="number">1000</div>
#</li>
#<li class="primaryconsumerlist">
#<div class="name">rabbit</div>
#<div class="number">2000</div>
#</li>
#</ul>
#<li class="primaryconsumerlist">
#<div class="name">deer</div>
#<div class="number">1000</div>
#</li>
#<div class="name">deer</div>
#<div class="number">1000</div>
#<li class="primaryconsumerlist">
#<div class="name">rabbit</div>
#<div class="number">2000</div>
#</li>
#<div class="name">rabbit</div>
#<div class="number">2000</div>
#<ul id="secondaryconsumers">
#<li class="secondaryconsumerlist">
#<div class="name">fox</div>
#<div class="number">100</div>
#</li>
#<li class="secondaryconsumerlist">
#<div class="name">bear</div>
#				[ 28 ]
#				www.it-ebooks.infoChapter 3
#				<div class="number">100</div>
#</li>
#</ul>
#<li class="secondaryconsumerlist">
#<div class="name">fox</div>
#<div class="number">100</div>
#</li>
#<div class="name">fox</div>
#<div class="number">100</div>
#<li class="secondaryconsumerlist">
#<div class="name">bear</div>
#				[ 28 ]
#				www.it-ebooks.infoChapter 3
#				<div class="number">100</div>
#</li>
#<div class="name">bear</div>
#<div class="number">100</div>
#<ul id="tertiaryconsumers">
#<li class="tertiaryconsumerlist">
#<div class="name">lion</div>
#<div class="number">80</div>
#</li>
#<li class="tertiaryconsumerlist">
#<div class="name">tiger</div>
#<div class="number">50</div>
#</li>
#</ul>
#<li class="tertiaryconsumerlist">
#<div class="name">lion</div>
#<div class="number">80</div>
#</li>
#<div class="name">lion</div>
#<div class="number">80</div>
#<li class="tertiaryconsumerlist">
#<div class="name">tiger</div>
#<div class="number">50</div>
#</li>
#<div class="name">tiger</div>
#<div class="number">50</div>
#<ul id="quaternaryconsumers">
#<li class="quaternaryconsumerlist">
#<div class="name animal">tutle</div>
#<div class="number">1000</div>
#</li>
#<li class="quaternaryconsumerlist">
#<div class="name animal">giraffe</div>
#<div class="number">100</div>
#</li>
#</ul>
#<li class="quaternaryconsumerlist">
#<div class="name animal">tutle</div>
#<div class="number">1000</div>
#</li>
#<div class="name animal">tutle</div>
#<div class="number">1000</div>
#<li class="quaternaryconsumerlist">
#<div class="name animal">giraffe</div>
#<div class="number">100</div>
#</li>
#<div class="name animal">giraffe</div>
#<div class="number">100</div>

for e in soup.li.previous_elements:
    if isinstance(e, Tag):
        print(e)
