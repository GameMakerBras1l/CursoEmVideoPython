n1 = 0
n2 = 0
count = -1

while n1 != 999:
    print("Digite 999 quando quiser parar.")
    n1 = int(input("Digite um número: "))
    n2 = n1 + n2

    count += 1

n3 = n2 - 999

print("Você digitou {} veses, e as soma foi de {}".format(count, n3))