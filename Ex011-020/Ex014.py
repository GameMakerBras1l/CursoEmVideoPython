c = float(input('Infome uma temperattura em Celcius: '))

f = 1.8*c + 32

print('Em \033[32mFahrenheit\033[m, a temperatura é de \033[32m{:.2f}'.format(f))