n = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases de conversão
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')

op = int(input('Sua opção: '))

if op == 1:
    print('{} convertido para BINARIO é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n,oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n,hex(n)[2:]))
else:
    print('Opção invalida. Tente de novo.')