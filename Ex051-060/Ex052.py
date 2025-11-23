n = int(input("Digite um número: "))

count = 0

for c in range (1, n+1):
    if n%c == 0:
        count = count + 1

if count > 2:
    print(f"O {n} não é um número primo")
    
else:
    print(f"O {n} é um número primo")