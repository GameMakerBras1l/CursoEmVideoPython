import random
from time import sleep

print('Tente adinvinhar qual número a maquina vai escolher.')
rn = random.randint(1,5)

print('Carregando...')

sleep(3)
n = int(input('Digite um numero de 1 ate 5: '))

if n == rn:
    print('Você \033[32mACERTOU\033[m o número escolhido pela maquina :)')
else:
    print('Você \033[31mERROU\033[m o número que a maquina escolheu, o número era {}'.format(rn))