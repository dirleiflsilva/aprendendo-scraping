from bs4 import BeautifulSoup

# abrir arquivo para leitura
with open('arquivo01.html','r') as f:
    soup = BeautifulSoup(f,'lxml')

tag = soup.title
print(tag)
print(tag.name)

tag = soup.p
print(tag)
print(tag.name)
