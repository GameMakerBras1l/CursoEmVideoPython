import random
from time import sleep

x = 0
pc = random.randint(0,10)
"""use = -1"""
palp = 0

print("Vamos jogar um jogo tente adivinhar um número de 0 até 10")
print("")

acertou = False

"""while pc != use:

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
    print(f"Você precisou de {x} tentativas")"""

while not acertou:
    use = int(input("Qual seu paltpite: "))
    palp += 1
    if use == pc:
        acertou = True
    else:
        if use < pc:
            print("Mais...")
        elif use > pc:
            print("Menos...")

print("Acertou com {} tentarivas".format(palp))
