dias = int(input('Digite quantos dias você alugou o carro: '))
km = float(input('Digite quantos km vc pecorreu com o carro:  '))
preco = dias*60 + km*0.15

print('O aluguel do carro foi de \033[32mR${:.2f}\033[m'.format(preco))