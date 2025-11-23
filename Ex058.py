import random
from time import sleep

x = 0
pc = random.randint(0,10)
use = -1

print("Vamos jogar um jogo tente adivinhar um número de 0 até 10")
print("")

while pc != use:
    use = int(input("Digite un número de 0 até 10: "))
    print("")

    sleep(1)

    if pc != use:
        print("Você errou tente de novo")

    x += 1

print("")

if x < 6:
    print(f"Parabens vc acertou o número em {x} tentativas")

else:
    print(f"Você precisou de {x} tentativas")