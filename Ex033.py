from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))

x, y, z = '','',''

sleep(3)


if n1 > n2 >= n3 or n1 == n2 > n3:
    x, y, z = n3, n2, n1

elif n1 >= n3 > n2 or n1 > n3 == n2:
    x, y, z = n2, n3, n1

elif n2 >= n3 > n1 or n2 > n3 == n1:
    x, y, z = n1, n3, n2

elif n2 > n1 > n3:
    x, y, z = n3, n1, n2

elif n3 > n1 > n2:
    x, y, z = n2, n1, n3

elif n3 > n2 > n1:
    x, y, z = n1, n2, n3

else:
    x, y, z = n1, n2, n3

if n1 == n2 == n3:
    print('Você digitou apenos o número \033[32m{}\033[m'.format(n1))
else:
    print('Em ordem crescente fica \033[32m{}, {}, {}'.format(x,y,z))