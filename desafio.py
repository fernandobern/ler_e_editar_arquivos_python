'''
​DESAFIO Manipulação de Arquivos
Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
# Primeiro crie 3 listas
 * Uma lista que contem 5 frutas
 * Uma lista que contem 5 cores
 * Uma lista que contem 5 linguagens de programação
# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''


import os

lista_frutas = [
    'Laranja',
    'Morango',
    'Uva',
    'Maçao',
    'Abacaxi'
]

lista_cores = [
    'Vermelho',
    'Azul',
    'Roxo',
    'Preto',
    'Verde'
]

lista_linguagens = [
    'Python',
    'Java',
    'Kotlin',
    'Typescript',
    'Lua'
]

print('Criando lista_cores')
with open('Pesquisar-Salvar-Editar-Excluir/frutas.txt', 'w', encoding='utf-8', newline='') as arquivo:
    frutas_str = '\n'.join(lista_frutas)
    for fruta in lista_frutas:
        arquivo.write(f'{fruta}' + os.linesep)
print('Adicionando cores')
with open('Pesquisar-Salvar-Editar-Excluir/frutas.txt', 'a', encoding='utf-8', newline='') as arquivo:
    cores_str = '\n'.join(lista_frutas)
    for cor in lista_cores:
        arquivo.write(f'{cor}' + os.linesep)
        print(f'A cor {cor} foi adicionada')


with open('Pesquisar-Salvar-Editar-Excluir/cores.txt', 'r+', encoding='utf-8', newline='') as arquivo:
    cores_str = '\n'.join(lista_frutas)
    for cor in lista_cores:
        arquivo.write(f'{cor}' + os.linesep)
        



with open('Pesquisar-Salvar-Editar-Excluir/linguagens.txt', 'w', encoding='utf-8', newline='') as arquivo:
    linguagens_str = '\n'.join(lista_frutas)
    for linguagem in lista_linguagens:
        arquivo.write(f'{linguagem}' + os.linesep)

nome_arquivos = [
    'arquivo1', 'arquivo2', 'arquivo3', 'arquivo4', 'arquivo5'
]

for i in range(len(nome_arquivos)):
    with open(f'Pesquisar-Salvar-Editar-Excluir/arquivo{i}.txt', 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write(f"Conteúdo do {i}")
        print(f'Criando arquivo {i}')