from time import sleep

print('Calculo de prestação.')

sleep(1)

n1 = float(input('Bom dia, por favor digite o seu salario mensal antes de começarmos: '))

n2 = float(input('Agora digite o valor do emprestimo desejado: '))

a = int(input('Agora digite em quanto tempo (em anos) voce pretende pagar: '))

m = a*12

x = ''
y = ''
z = ''

n3 = (n1*30)/100 + n1

if m > 24:
    x = 0.12
else:
    x = 0.04

print('Calculando...')
sleep(3)

p1 = (((1 + x)**m)*x)/(((1 + x)**m) - 1)

p2 = p1*n2

if p2 > n3:
    y = '\033[31mnegado\033[m'
else:
    y = '\033[32maprovado\033[m'

if y == '\033[31mnegado\033[m':
    z = '\033[33m, devido a prestação mensal ultrapassar 30% de seu salario mensal\033[m'

print('Seu emprestimo foi {}{}'.format(y,z))