num = int(input("Digite um número para calcular o fatorial: "))
fat = 1

if num < 0:
        print("Fatorial não pode ser definido por números negativos.")

elif num == 0:
    print("O fatorial de 0 é 1")

else:
    num_original = num

    while num > 0:
        fat *= num
        num -= 1

    print(f"O Fatorial de {num_original} é {fat}")