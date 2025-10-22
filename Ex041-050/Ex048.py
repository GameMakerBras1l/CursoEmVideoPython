n = 0

for c in range(1, 500+1):
    if c%3 == 0:
        n = n + c

print(f"A soma de todos os números impares multiplos de três entre 1 e 500 é de {n}")