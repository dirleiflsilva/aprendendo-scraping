''' escrevendo em um arquivo

arq = open('arquivo.txt', 'w')
arq.write('Python eh legal\n')
arq.write('curso de BS4')
arq.close()
'''

''' lendo um arquivo
arq = open('arquivo.txt','r')
print(arq.read())
arq.close()
'''

# forma pythonica de ler arquivo
with open('arquivo.txt','r') as f:
    print(f.read())
