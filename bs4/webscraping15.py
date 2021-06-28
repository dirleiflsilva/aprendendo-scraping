"""
parseando arquivo html
buscando elementos com find_next/find_all_next/find_previous/find_all_previous
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo03.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')

producers = soup.find(id = 'producers')
tag_next = producers.find_next()
print(tag_next)
"""
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
"""

producers = soup.find(id = 'producers')
tag_next = producers.find_all_next()
print(tag_next)
"""
[<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>, <div class="name">plants</div>, <div class="number">100000</div>, <li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>, <div class="name">algae</div>, <div class="number">100000</div>, <ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>, <li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>, <div class="name">deer</div>, <div class="number">1000</div>, <li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>, <div class="name">rabbit</div>, <div class="number">2000</div>, <ul id="secondaryconsumers">
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
</ul>, <li class="secondaryconsumerlist">
<div class="name">fox</div>
<div class="number">100</div>
</li>, <div class="name">fox</div>, <div class="number">100</div>, <li class="secondaryconsumerlist">
<div class="name">bear</div>
				[ 28 ]
				www.it-ebooks.infoChapter 3
				<div class="number">100</div>
</li>, <div class="name">bear</div>, <div class="number">100</div>, <ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>, <li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>, <div class="name">lion</div>, <div class="number">80</div>, <li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>, <div class="name">tiger</div>, <div class="number">50</div>, <ul id="quaternaryconsumers">
<li class="quaternaryconsumerlist">
<div class="name animal">tutle</div>
<div class="number">1000</div>
</li>
<li class="quaternaryconsumerlist">
<div class="name animal">giraffe</div>
<div class="number">100</div>
</li>
</ul>, <li class="quaternaryconsumerlist">
<div class="name animal">tutle</div>
<div class="number">1000</div>
</li>, <div class="name animal">tutle</div>, <div class="number">1000</div>, <li class="quaternaryconsumerlist">
<div class="name animal">giraffe</div>
<div class="number">100</div>
</li>, <div class="name animal">giraffe</div>, <div class="number">100</div>]
"""

producers = soup.find(id = 'quaternaryconsumers')
tag_previous = producers.find_previous()
print(tag_previous)

#<div class="number">50</div>

producers = soup.find(id = 'quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)
"""
[<div class="number">50</div>, <div class="name">tiger</div>, <li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>, <div class="number">80</div>, <div class="name">lion</div>, <li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>, <ul id="tertiaryconsumers">
<li class="tertiaryconsumerlist">
<div class="name">lion</div>
<div class="number">80</div>
</li>
<li class="tertiaryconsumerlist">
<div class="name">tiger</div>
<div class="number">50</div>
</li>
</ul>, <div class="number">100</div>, <div class="name">bear</div>, <li class="secondaryconsumerlist">
<div class="name">bear</div>
				[ 28 ]
				www.it-ebooks.infoChapter 3
				<div class="number">100</div>
</li>, <div class="number">100</div>, <div class="name">fox</div>, <li class="secondaryconsumerlist">
<div class="name">fox</div>
<div class="number">100</div>
</li>, <ul id="secondaryconsumers">
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
</ul>, <div class="number">2000</div>, <div class="name">rabbit</div>, <li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>, <div class="number">1000</div>, <div class="name">deer</div>, <li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>, <ul id="primaryconsumers">
<li class="primaryconsumerlist">
<div class="name">deer</div>
<div class="number">1000</div>
</li>
<li class="primaryconsumerlist">
<div class="name">rabbit</div>
<div class="number">2000</div>
</li>
</ul>, <div class="number">100000</div>, <div class="name">algae</div>, <li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>, <div class="number">100000</div>, <div class="name">plants</div>, <li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>, <ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>, <div class="ecopyramid">
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
</div>, <body>
<div class="ecopyramid">
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
</div>
</body>, <html>
<body>
<div class="ecopyramid">
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
</div>
</body>
</html>]
"""
