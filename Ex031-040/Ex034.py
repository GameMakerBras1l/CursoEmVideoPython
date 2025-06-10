sal = float(input('Informe seu salario para calcular o aumento: '))

x = ''

if sal > 1250:
    x = 10
else:
    x = 15

a = (sal*x)/100

print('Com um aumento de \033[32m{}%\033[m, o novo salario com um acrescimo'
      ' de \033[32mR${:.2f}\033[m, é de \033[32mR${:.2f}'.format(x,a,(sal + a)))