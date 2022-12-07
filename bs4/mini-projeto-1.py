"""
Projeto Saraiva
Baixando o conteúdo da página
Obtendo a lista de produtos
Obtendo a página do produto
Obtendo outros dados do produto
"""
# importando modulos
import requests
from bs4 import BeautifulSoup

"""
Criar função para realizar a requisição de uma página
Busca por palavra chave
"""

def get_http(url, palavra):

    palavra = palavra #palavra.replace(' ','%20')
    url = '{0}?q={1}'.format(url, palavra)

    # tratando exceções
    try:
        return requests.get(url)
    except(requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
    except Exception as e:
        raise

# Obtendo a lista de produtos
def get_produtos(content):

    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('div',{'class':'nm-product-info'})

    # criar lista vazia
    lista_produtos = []
    for produto in produtos:
        info_produto = [produto.a.get('href'), produto.a.string]
        lista_produtos.append(info_produto)
    return lista_produtos

# buscar a página do produto
def get_page_produto(lista_produtos):

    d = {}
    lista_prod = []

    for produto in lista_produtos:
        # tratando exceções
        try:
            # produto[0] = '//www.saraiva.com.br/box-harry-potter-edicao-tradicional-serie-completa-10678733/p'
            r = requests.get('https:'+ produto[0])
        except(requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
               requests.exceptions.Timeout) as e:
            print(str(e))
            r = None
        except Exception as e:
            raise

        d = parser_page_produto(r.text, 'https:'+ produto[0], produto[1])
        lista_prod.append(d.copy())

        return lista_prod

def parser_page_produto(content, url_produto, titulo):

    soup = BeautifulSoup(content, 'lxml')
    div = soup.find('div', {'class':'tab-content pt-0'})
    url_capa = div.img.get('src')
    preco = soup.find('p',{'class':'mb-0 price-destaque'})
    d = {}
    try:
        preco = preco.string
        d = {
            'Título ': titulo,
            'Preco ': preco,
            'URL Capa ': url_capa,
            'URL Produto ': url_produto
        }
    except AttributeError as e:
        print(str(e))

    return d

if __name__ == '__main__':

    url = 'http://busca.saraiva.com.br/busca'
    palavra = 'harry porter'

    r = get_http(url, palavra)
    if r:
        lista_produtos = get_produtos(r.text)
        lista = get_page_produto(lista_produtos)
        print(lista)