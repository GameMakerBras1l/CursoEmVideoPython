from random import shuffle, random

n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite um terceiro nome: ')
n4 = input('Digite o quarto nome: ')

nomes = [n1, n2, n3, n4]
shuffle(nomes)

print('A ordem de apresentação será: \033[32m{}'.format(nomes))