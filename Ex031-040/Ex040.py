n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2)/2

x = ''
y = ''

if media < 5:
    x = '\033[31mREPROVADO\033[m'
    y = '\033[31m{:.2f}\033[m'.format(media)
elif 5 <= media < 7:
    x = '\033[33mEM RECUPERAÇÃO\033[m'
    y = '\033[33m{:.2f}\033[m'.format(media)
else:
    x = '\033[32mAPROVADO\033[m'
    y = '\033[32m{:.2f}\033[m'.format(media)

print('O Aluno Esta {} com a media {}'.format(x,y))