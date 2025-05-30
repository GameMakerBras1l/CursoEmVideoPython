sal = float(input('Digite o Seu Salario: '))

au = (sal*15)/100
nsal = sal + au

print('Com um acrecimo de \033[32m15%\033[m o novo salario é de \033[32mR${:.2f}\033[m'.format(nsal))