"""
parseando arquivo html
"""
# importando modulo requests
import requests
# importando modulo BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

'''
# usando with para garantir a finalização do processo/recurso
with open('arquivo01.html','r') as file: # r = read
    soup_string = BeautifulSoup(file.read(),'html.parser') # parser padrão do bs4
print(soup_string)
'''

"""
utilizando parser lxml em uma página web
"""
'''
r = requests.get('http://www.pudim.com.br')
soup_string = BeautifulSoup(r.text,'lxml')
print(soup_string)
'''

"""
utilizando parser html5lib
"""
with open('arquivo01.html','r') as f:
    soup_string = BeautifulSoup(f.read(),'html5lib')
print(soup_string)
