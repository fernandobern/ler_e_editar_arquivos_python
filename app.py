"""
COM CRIAR E MODIFICAR ARQUIVOS:
'r' - usado somente para leitura
'w' - usado somente para escrever algo
'r+' - usado para ler e escrever algo
'a' - usado para acrescentar algo

"""

import os

#print(os.getcwd())

""" 
#Criando arquivo com 'w', e escrevendo uma informação
with open('Pesquisar-Salvar-Editar-Excluir/celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 1')#Isso é o que será escrito no arquivo
"""

"""
#Acrescentando informações ao arquivo usando 'a'
with open('Pesquisar-Salvar-Editar-Excluir/nomes.txt', 'a') as arquivo:
    arquivo.write('Luiz') 
"""

""" 
#Acrescentando informações de liSTA e quebrando linha
nomes = [
   'Maria',
   'Joao',
   'Ana',
   'Pedro',
   'Clara',
   'Rafael',
   'Fernando',
   'Lucas',
   'Laura',
   'Gustavo'
]
#passando arquivo a ser criado ou acrescentado as informações
with open('Pesquisar-Salvar-Editar-Excluir/nomes.txt', 'a', newline='') as arquivo:
    #Criando loop para acrescentar cada nome da lista no arquivo
    for nome in nomes:
        arquivo.write(nome + os.linesep)
#ATENÇÃO, CASO SEJA LISTA DE NÚMERO TEM QUE CONVERTER PARA STRING
"""

""" 
#Lendo arquivos
with open('Pesquisar-Salvar-Editar-Excluir/nomes.txt', 'r') as arquivo:
    for nome in arquivo:
        print(nome)
"""

#Ler e escrever informações em um arquivo 
with open('Pesquisar-Salvar-Editar-Excluir/nomes.txt', 'r+', newline='') as arquivo:
    for nome in arquivo:
        print(nome)
    arquivo.write('Fulano' + os.linesep)