n = int(input("Digite um Número qualquer: "))

print(f"A tabuada de {n} é: ")

print("====================")

for c in range(1, 10+1):
    print(c, ' X ', n, ' = ',c*n)

print("====================")
