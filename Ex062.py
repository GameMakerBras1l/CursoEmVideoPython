termo = int(input("Digite o Termo: "))

razao = int(input("Digite a Razão: "))

count = 1
total = 0
mais = 10


while mais != 0:
    total = total + mais
    while count <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        count += 1

    print("PAUSA")

    mais = int(input("Quantos a mais vc quer mostrar? "))


print("FIM DA PA")