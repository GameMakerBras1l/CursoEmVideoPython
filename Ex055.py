"""pesos = [0, 0, 0, 0, 0]

for c in range(0, 5):
    pesos[c] = float(input("Digite um peso: "))

pesos.sort()
print(f"Os pesos foram {pesos}")"""

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Peso da {}* pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior}")
print(f"O menor peso lido foi {menor}")