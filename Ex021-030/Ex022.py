from time import sleep

n = input('Digite seu nome completo: ')
n1 = n.split()

print('Analisando...')
sleep(2)

print('Seu nome em maisculo é \033[32m{}\033[m'.format(n.upper()))
print('Seu nome em minusculo é \033[32m{}\033[m'.format(n.lower()))
print('Seu nome tem \033[32m{}\033[m letras'.format(len(n.strip())))
print('O seu primeiro nome é \033[32m{}'.format(n1[0]))