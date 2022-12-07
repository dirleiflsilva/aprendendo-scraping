"""
usando Requests
redirecionamento (response)
"""
# importando modulo Requests
import requests

#url = 'http://www.google.com'
#<Response [200]>
url = 'http://dirlei.com.br'
#Connection
#HTTPConnectionPool(host='www.codidados.com.br', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fdeb0330700>: Failed to establish a new connection: [Errno -2] Name or service not known'))

try:
    r = requests.get(url)
    print(r)
#except requests.exceptions.ConnectionError as e:
#except requests.exceptions.HTTPError as e:
#except requests.exceptions.Timeout as e:
#except requests.exceptions.TooManyRedirects as e:
except requests.exceptions.RequestException as e:
    print('Connection')
    print(str(e))