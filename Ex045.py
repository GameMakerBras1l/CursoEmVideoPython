import random

print('Vamos jogar Jokenpo.')

m = random.randint(1,3)

n = int(input('Por favor, digite um número para escolher sua mão, \033[32mPedra é'
                  ' 1\033[m, o \033[32mPapel é 2\033[m e a \033[32mTesoura é 3\033[m: '))

while n < 1 or n > 3:
    print('Voce não digitou um dos números solicitados.')
    n = int(input('Por favor digite o correto dessa vez: '))

if m == 1 and n == 2:
    print('Papel ganha de Pedra, você \033[32mGANHOU!!!\033[m')
elif m == 1 and n == 3:
    print('Pedra ganha de Tesoura, você \033[31mPERDEU.\033[m')
elif m == 2 and n == 3:
    print('Tesoura ganha de Papel, você \033[32mGANHOU!!!\033[m')
elif m == 2 and n == 1:
    print('Papel ganha de pedra, você \033[31mPERDEU.\033[m')
elif m == 3 and n == 1:
    print('Pedra ganha de Tesoura, você \033[32mGANHOU!!!\033[m')
elif m == 3 and n == 2:
    print('Tesoura ganha de Papel, você \033[31mPERDEU.\033[m')
else:
    print('Deu empate. ')