"""
usando Requests
trabalhando com proxies
"""
# importando modulo Requests
import requests

# proxies free
# http://www.ultrapoxies.com/
# https://www.hide-my-ip.com/pt/proxylist.shtml

url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'
#proxies = {'https':'169.57.157.148:8123'}
proxies = {'http':'183.181.164.210:80'}

try:
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
except requests.exceptions.ConnectionError as e:
    print(str(e)