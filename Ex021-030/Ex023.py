n = int(input('Digite um número inteiro de no maximo quatro digitos: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: \033[32m{}\033[m'.format(u))
print('Dezena: \033[32m{}\033[m'.format(d))
print('Centena: \033[32m{}\033[m'.format(c))
print('Milhar: \033[32m{}\033[m'.format(m))