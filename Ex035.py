l1 = float(input('Digite um lado para formar um triângulo: '))
l2 = float(input('Digite mais um: '))
l3 = float(input('Agora digite o terceiro número: '))

x = ''

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    x = 'É'
else:
    x = 'Não é'

print('\033[32m{}\033[m possivel formar um triângulo com esses trÊs lados.'.format(x))