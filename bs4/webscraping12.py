"""
parseando arquivo html
buscando elementos com find_all
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo03.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag_list = soup.find_all('ul')
print(tag_list)
"""
[<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
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

tag_list = soup.find_all(['ul','div'])
print(tag_list)
"""
[<div class="ecopyramid">
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
</div>, <ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>, <div class="name">plants</div>, <div class="number">100000</div>, <div class="name">algae</div>, <div class="number">100000</div>, <ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>, <div class="name">deer</div>, <div class="number">1000</div>, <div class="name">rabbit</div>, <div class="number">2000</div>, <ul id="secondaryconsumers">
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
</ul>, <div class="name">fox</div>, <div class="number">100</div>, <div class="name">bear</div>, <div class="number">100</div>, <ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>, <div class="name">lion</div>, <div class="number">80</div>, <div class="name">tiger</div>, <div class="number">50</div>, <ul id="quaternaryconsumers">
<li class="quaternaryconsumerlist">
<div class="name animal">tutle</div>
<div class="number">1000</div>
</li>
<li class="quaternaryconsumerlist">
<div class="name animal">giraffe</div>
<div class="number">100</div>
</li>
</ul>, <div class="name animal">tutle</div>, <div class="number">1000</div>, <div class="name animal">giraffe</div>, <div class="number">100</div>]
"""

tag_list = soup.find_all('ul',limit = 2)
print(tag_list)
"""
[<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
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
</ul>]
"""

tag_list = soup.find_all(string = 'rabbit')
print(tag_list)

#['rabbit']

# retorna todos os textos
tag_list = soup.find_all(string=True)
print(tag_list)

#['html', '\n', '\n', '\n', '\n', '\n', 'plants', '\n', '100000', '\n', '\n', '\n', 'algae', '\n', '100000', '\n', '\n', '\n', '\n', '\n', 'deer', '\n', '1000', '\n', '\n', '\n', 'rabbit', '\n', '2000', '\n', '\n', '\n', '\n', '\n', 'fox', '\n', '100', '\n', '\n', '\n', 'bear', '\n\t\t\t\t[ 28 ]\n\t\t\t\twww.it-ebooks.infoChapter 3\n\t\t\t\t', '100', '\n', '\n', '\n', '\n', '\n', 'lion', '\n', '80', '\n', '\n', '\n', 'tiger', '\n', '50', '\n', '\n', '\n', '\n', '\n', 'tutle', '\n', '1000', '\n', '\n', '\n', 'giraffe', '\n', '100', '\n', '\n', '\n', '\n', '\n', '\n']

tag_list = soup.find_all(string=['rabbit','bear'])
print(tag_list)

#['rabbit', 'bear']

tag_list = soup.find_all(class_ = ['producerlist','primaryconsumerlist'])
print(tag_list)
"""
[<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>, <li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>, <li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>, <li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>]
"""

tag_list = soup.ul.find_all('div')
print(tag_list)

#[<div class="name">plants</div>, <div class="number">100000</div>, <div class="name">algae</div>, <div class="number">100000</div>]

tag_list = soup.find_all('div', class_ = 'name')
print(tag_list)

#[<div class="name">plants</div>, <div class="name">algae</div>, <div class="name">deer</div>, <div class="name">rabbit</div>, <div class="name">fox</div>, <div class="name">bear</div>, <div class="name">lion</div>, <div class="name">tiger</div>, <div class="name animal">tutle</div>, <div class="name animal">giraffe</div>]
