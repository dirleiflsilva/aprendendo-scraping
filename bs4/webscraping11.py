"""
parseando arquivo html
buscando elementos com find
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo04.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.find('li')
print(tag)

#<li class="parent_producerlist">
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
#<ul id="secondaryconsumers">
#<li class="secondaryconsumerlist">
#<div class="name">fox</div>
#<div class="number">100</div>
#</li>
#<li class="secondaryconsumerlist">
#<div class="name">bear</div>
#						[ 28 ]
#						www.it-ebooks.infoChapter 3
#						<div class="number">100</div>
#</li>
#</ul>
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
#</li>

tag = soup.find(string = 'plants')
print(tag)

#plants

tag = soup.find(id = 'secondaryconsumers')
print(tag)

#<ul id="secondaryconsumers">
#<li class="secondaryconsumerlist">
#<div class="name">fox</div>
#<div class="number">100</div>
#</li>
#<li class="secondaryconsumerlist">
#<div class="name">bear</div>
#						[ 28 ]
#						www.it-ebooks.infoChapter 3
#						<div class="number">100</div>
#</li>
#</ul>

tag = soup.find(attrs={'class':'primaryconsumerlist'})
print(tag)

#<li class="primaryconsumerlist">
#<div class="name">deer</div>
#<div class="number">1000</div>
#</li>

tag = soup.find(class_ = 'primaryconsumerlist')
print(tag)

#<li class="primaryconsumerlist">
#<div class="name">deer</div>
#<div class="number">1000</div>
#</li>

tag = soup.find('ul', attrs = {'class':'producerlist'})
print(tag)

#None

tag = soup.find('li', attrs = {'class':'producerlist'})
print(tag)

#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>

tag = soup.ul.li.find('li')
print(tag)

#<li class="producerlist">
#<div class="name">plants</div>
#<div class="number">100000</div>
#</li>

def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)

#fox