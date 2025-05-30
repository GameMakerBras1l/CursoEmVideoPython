v = int(input('Digite a velocidade do carro: '))

ma = 120.00 + (v - 80)*7
mb = 90.00 + (40 - v)*7

if v > 80:
    print('Você foi \033[31mmultado\033[m por causa do exesso '
          'de velocidade, sua multa foi de R${:.2f}'.format(ma))
elif v < 40:
    print('Você foi \033[31mmultado\033[m por baixa velocidade, sua multa foi de R${}'.format(mb))
else:
    print('\033[32mPARABENS\033[m, você não foi multado.')