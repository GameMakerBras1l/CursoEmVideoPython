print('{:=^40}'.format(' LOJA CIRO DA PENHA '))

p = float(input('Digite o preço do produto desejado (minimo 10 reais): '))

while p <= 9.99:
    p = float(input('Você não digitou o valor minimo, digite novamente: '))

x = int(input('Digite a forma de pagamento, a vista por dinheiro/check com 10% de desconto \033[33mdigite 1\033[m, para a'
              'vista com o cartão com 5% dde desconto \033[33mdigite 2\033[m, se for por parcelamento no cartão '
              '\033[33mdigite 3\033[m: '))

p2 = ''
p3 = ''
pa = ''
y = ''
z = ''

if x == 1:
    p2 = p - p/10
elif x == 2:
    p2 = p - p/20
elif x == 3:
    y = int(input('Você escolheu a opção com parcelamento, se deseja 2x no cartão, como o preço normal, '
                  '\033[33mdigite 1\033[m, mas se quiser 3x ou mais no cartão, com 20% de juros '
                  '\033[33mdigite 2\033[m: '))
    z = 1

if y == 1:
    p2 = p
    p3 = p2/2
    pa = 2
elif y == 2:
    pa = int(input('Você escolheu pagar 3 ou mais, digite o numero desejado de parcelas: '))
    p2 = p + p/5
    p3 = p2/pa

if z == 1:
    print('O preço total da compra é de R$\033[32m{:.2f}\033[m, '
          'com \033[32m{}\033[m parcelas de R$\033[32m{:.2f}\033[m'.format(p2, pa, p3))
else:
    print('O preço total do produto é de R$\033[32m{:.2f}\033[m'.format(p2))