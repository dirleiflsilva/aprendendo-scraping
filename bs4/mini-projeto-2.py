"""
Projeto Editora Novatec
Baixando o conteúdo da página
Obtendo a lista de produtos
Obtendo a página do produto
"""
# importando modulos
import requests
from bs4 import BeautifulSoup

"""
Criar função para realizar a requisição de uma página
Busca por palavra chave
"""

def post_http(url, nome_livro):

    payload = {'palavra': nome_livro,'enviar':'Buscar'}

    try:
        return requests.post(url,data=payload)
    except(requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
           requests.exceptions.Timeout) as e:
        print(str(e))
    except Exception as e:
        raise
    return None

def parser_html(content):

    soup = BeautifulSoup(content, 'lxml')

    produtos = soup.find_all('table')[10].find_all('td')
    """
    f = open('teste/content-td.html','w')

    for produto in produtos:
        f.write(str(produto))
        f.write('\n\n\n')

    f.close()
    """
    lista_produtos = []
    url = 'https://www.novatec.com.br'
    url_capa = ''
    url_produto = ''
    for produto in produtos:
        tag_a = produto.find('a')
        if tag_a:
            if tag_a.next_element.next_element.img.name == 'img':
                url_capa = tag_a.img.get('src')
                url_produto = tag_a.get('href')
                lista_produtos.append(url_capa)
                lista_produtos.append(url_produto)

        for string in produto.stripped_strings:
            if (string == 'Esgotado'):
                continue
            lista_produtos.append(string)
    print(lista_produtos)

if __name__ == '__main__':

    url = 'https://novatec.com.br/busca.php'
    #nome_livro = input('Nome do livro: ')
    nome_livro = 'redes de computadores'

    r = post_http(url, nome_livro)

    if r:
        parser_html(r.text)