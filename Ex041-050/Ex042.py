l1 = float(input('Digite um lado: '))
l2 = float(input('Digite outro lado: '))
l3 = float(input('Digite um terceiro lado: '))

x = ''
y = 0
z = ''

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    x = '\033[32mÉ\033[m'
    y = 1
else:
    x = '\033[31mNão é\033[m'

print('{} possivel formar um triangulo com esses lados'.format(x))

if l1 == l2 == l3:
    z = '\033[32mequilátero\033[m'
elif l1 == l2 or l2 == l3 or l3 == l1:
    z = '\033[32misóceles\033[m'
else:
    z = '\033[32mescaleno\033[m'

if y == 1:
    print('O triangulo formado é um {}'.format(z))