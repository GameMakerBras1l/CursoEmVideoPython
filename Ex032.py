n = int(input('Digite um ano: '))

x = ''
if n % 4 == 0 and n % 100 != 0:
    x = 'é'
elif n % 400 == 0:
    x = 'é'
else:
    x = 'não é'

print('O ano \033[32m{}, {}\033[m ano bissexto.'.format(n,x))