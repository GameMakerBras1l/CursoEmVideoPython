pesos = [0, 0, 0, 0, 0]

for c in range(0, 5):
    pesos[c] = int(input("Digite um peso: "))

pesos.sort()
print(f"Os pesos foram {pesos}")