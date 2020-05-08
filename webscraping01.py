import requests
from bs4 import BeautifulSoup

'''
with open('arquivo01.html','r') as f:
    soup_string = BeautifulSoup(f.read(),'html.parser') # parser padrão do bs4
print(soup_string)
'''

'''
r = requests.get('http://www.pudim.com.br')
soup_string = BeautifulSoup(r.text,'lxml') # parser lxml
print(soup_string)
'''

with open('arquivo01.html','r') as f:
    soup_string = BeautifulSoup(f.read(),'html5lib') # parser html5lib
print(soup_string)
