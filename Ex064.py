n1 = n2 = count = 0

n1 = int(input("Digite um número [999 para parar]: "))

while n1 != 999:
    n1 = int(input("Digite um número [999 para parar]: "))
    n2 = n1 + n2

    count += 1

n3 = n2 - 999

print("Você digitou {} veses, e as soma " \
"foi de {}".format(count, n3))