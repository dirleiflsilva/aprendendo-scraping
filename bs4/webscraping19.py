"""
usando Requests
"""
# importando modulo Requests
import requests
from bs4 import BeautifulSoup

url = 'http://michaelis.uol.com.br/busca?'
payload = {'r':'0',
           'f':'0',
           't':'0',
           'palavra': 'talk'}

# enviar um header customizado
header = { '(Request-Line)':'GET /moderno-portugues/busca/portugues-brasileiro/talk/ HTTP/2',
           'Host': 'michaelis.uol.com.br',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'pt-BR,pt;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Connection': 'keep-alive',
           'Referer': 'http://michaelis.uol.com.br/',
           'Upgrade-Insecure-Requests': '1'
        }

r = requests.get(url, payload, headers = header)
print(r.text)

with open('./teste/michaelis.html', 'w') as f:
    f.write(r.text)

print(r.request.headers)
# {'User-Agent': 'python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

soup = BeautifulSoup(r.text, 'lxml')
div = soup.find('div', {'id': 'content'})
print(div)
"""
<div class="col-lg-8 col-md-8" id="content">
<div class="verbete bs-component">
<e2>talk show</e2> <br/><et>[tɔ:k ʃoʊ]</et><br/><br/><cg>sm</cg><br/><ra>Rád</ra>, <ra>TV</ra> Programa de entrevistas e/ou debates, frequentemente intercalados com apresentações artísticas de diversos gêneros.<br/><sm>ETIMOLOGIA</sm><i>ingl</i>.
  </div>
</div>
"""
print(div.get_text())
# talk show [tɔ:k ʃoʊ]smRád, TV Programa de entrevistas e/ou debates, frequentemente intercalados com apresentações artísticas de diversos gêneros.ETIMOLOGIAingl.
