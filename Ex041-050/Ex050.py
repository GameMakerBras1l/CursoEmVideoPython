soma = 0

for c in range(0, 6):
    n = int(input("Digite um número: "))

    if n%2 == 0:
        soma = soma + n

if soma == 0:
    print("Vc não digitou nenhum número par")
else:
    print(f"A soma de todos os numeros pares digitados é de {soma}")