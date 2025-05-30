from datetime import date

h = date.today().year
p = ''
p2 = ''

anoN = int(input('Digite o ano de nassimento do jovem: '))

if h - anoN < 18:
    p = '\033[31mNão pode se\033[m'
elif h - anoN == 18:
    p = '\033[32mDeve se\033[m'
else:
    p = '\033[33mJá passou do tempo de se\033[m'

if h - anoN < 18:
    p2 = ', faltam {} ano(s) para o alistamento'.format(18 - (h - anoN))
elif h - anoN > 18:
    p2 = ', ja passou {} ano(s) do alistemento'.format((h - anoN) - 18)


print('{} alistar{}'.format(p,p2))