"""
usando Requests
JSON Response
"""
# importando modulo Requests
import requests

url = 'http://compras.dados.gov.br'
cnpj = '07689002000189' # Embraer

# exemplo site
#http://compras.dados.gov.br/contratos/v1/contratos.html?uasg=20001&order_by=data_assinatura&order=desc

url = '{0}/contratos/v1/contratos.json?cnpj_contratada={1}'.format(url, cnpj)

r = requests.get(url)
print(r.json()['_embedded']['contratos'][0])
