"""
parseando arquivo html / tag
parser lxml
"""
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo01.html','r') as f:
    soup = BeautifulSoup(f,'lxml')

# busca primeira ocorrencia title
tag = soup.title
print(tag)
print(tag.name) # nome da tag = title

tag = soup.p
print(tag)
print(tag.name)

'''
saída das tags
### title
<title>
    The Dormouse's story
   </title>
title

### p
<p class="title">
<b>
     The Dormouse's story
   </b>
</p>
p
'''
