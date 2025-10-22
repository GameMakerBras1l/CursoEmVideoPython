from datetime import date

n1 = int(input('Digite o ano de nascimento do atleta: '))

n2 = date.today().year

n3 = n2 - n1

x = ''

if n3 <= 9:
    x = '\033[32mmirim\033[m'
elif 9 < n3 <= 14:
    x = '\033[32minfantil\033[m'
elif 14 < n3 <= 19:
    x = '\033[32mjuvenil\033[m'
elif 19 < n3 <= 25:
    x = '\033[32msenior\033[m'
elif n3 > 25:
    x = '\033[32mmaster\033[m'

print('A liga desse atleta é {}'.format(x))