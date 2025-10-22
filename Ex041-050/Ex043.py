a = float(input('Informe a sua altura: '))
p = float(input('Informe o seu peso: '))

imc = p/(a**2)

x = ''

if imc < 18.5:
    x = '\033[33mabaixo do peso\033[m'
elif 18.5 <= imc < 25:
    x = '\033[32mcom o peso ideal\033[m'
elif 25 <= imc < 30:
    x = '\033[33mcom sobrepeso\033[m'
elif 30 <= imc < 40:
    x = '\033[33mcom obesidade\033[m'
else:
    x = '\033[31mcom obesidade morbida\033[m'

print('Seu IMC é de {:.2f}, você esta {}'.format(imc,x))