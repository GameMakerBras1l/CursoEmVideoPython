n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('O \033[32m{}\033[m é maior que \033[32m{}\033[m'.format(n1,n2))
elif n2 > n1:
    print('O \033[32m{}\033[m é maior que \033[32m{}\033[m'.format(n2,n1))
else:
    print('\033[32mNão existe valor maior,\033[m os dois são iguais.')