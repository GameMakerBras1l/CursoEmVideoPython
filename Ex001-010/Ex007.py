n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

if m >= 7:
    print('O aluno \033[32mPASSOU\033[m com a média {}, opa :)'.format(m))
elif 7 > m > 3:
    print('O aluno entrou em \033[33mRECUPERAÇÃO\033[m com a média {}'.format(m))
else:
    print('O aluno \033[31mREPROVOU\033[m com a média {} :('.format(m))