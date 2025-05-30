p = float(input('Digite o preço do produto: '))

d = p/20
np = p - d

print('Com um desconto de \033[32m5%\033[m sendo igual '
      'á \033[32mR${:.2f}\033[m, o novo preço vai ser \033[32mR${:.2f}\033[m'.format(d, np))