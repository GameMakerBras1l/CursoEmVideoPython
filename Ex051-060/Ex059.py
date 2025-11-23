x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = 0

while z != 5:

    print("[1]somar")
    print("[2]multiplicar")
    print("[3]maior")
    print("[4]novos números")
    print("[5]sair do programa")

    z = int(input("Escolha uma das opções acima: "))

    if z == 1:
        soma = x + y
        print(soma)
    
    elif z == 2:
        mult = x*y
        print(mult)

    elif z == 3:
        if x > y:
            print(f"{x} é maior que {y}")

        elif y > x:
            print(f"{y} é maior que {x}")

        else:
            print("Números iguais")

    elif z == 4:
        x = int(input("Digite um novo número: "))
        y = int(input("Digite um outro novo número: "))

print("Fim do programa")