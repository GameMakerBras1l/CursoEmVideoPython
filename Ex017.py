import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjecente: '))

h = math.sqrt(pow(co,2) + pow(ca,2))

print('A hipotenusa é \033[32m{:.2f}'.format(h))