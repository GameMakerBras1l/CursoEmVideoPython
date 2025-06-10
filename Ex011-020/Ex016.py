from math import trunc

n = float(input('Digite um número real: '))

print('O número digitaado foi {} e sua parte inteira é \033[32m{}\033[m'.format(n, trunc(n)))