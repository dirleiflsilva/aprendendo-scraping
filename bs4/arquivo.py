"""
Manipulação de arquivos

escrevendo em um arquivo
"""

arq = open('arquivo.txt', 'w') # w para escrever
arq.write('Python é legal\n') # \n = quebra de linha
arq.write('curso de BS4\n')
arq.write('Estou aprendendo a programar em Python!')
arq.close()


"""
Manipulação de arquivos

lendo um arquivo
"""
'''
arq = open('arquivo.txt','r') # r para ler
print(arq.read())
arq.close()
'''

"""
Manipulação de arquivos

forma pythonica de ler arquivo
"""

with open('arquivo.txt','r') as file:
    print(file.read())
