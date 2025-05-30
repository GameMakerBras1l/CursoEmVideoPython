n = int(input('Digite um número inteiro: '))

x = ''

if n%2 == 0:
    x = 'par'
else:
    x = 'impar'

print('O número digitado é um número \033[32m{}'.format(x))