n = int(input('Digite um número: '))

d = 2*n
t = 3*n
r = pow(n, 1/2)

print('Dobro: \033[32m{}\033[m'.format(d))
print('Triplo: \033[32m{}\033[m'.format(t))
print('Raiz Quadrada: \033[32m{:.2f}'.format(r))