num = int(input("Digite um numero qualquer: "))

x = 0

y = 1

z = 0

c = 0

print("Sequencia de Fibonacci")

while c < num:
    z = x + y

    print(z)

    x = z

    c +=1