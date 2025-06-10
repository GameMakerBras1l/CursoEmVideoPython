import random

a = input('Digite um nome: ')
a2 = input('Digite outro nome: ')
a3 = input('Digite mais um nome: ')
a4 = input('Digite um quarto: ')

nome = [a, a2, a3, a4]

aluno = random.choice(nome)

print('O nome sorteado é \033[32m{}'.format(aluno))