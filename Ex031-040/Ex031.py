n = int(input('Digite quanto quilometros você pretende viajar: '))

x = ''

if n <= 200:
    x = 0.50
else:
    x = 0.45

p = n*x

print('O preço de sua viagem é de R$\033[32m{}'.format(p))