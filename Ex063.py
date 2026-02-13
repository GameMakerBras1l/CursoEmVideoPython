print("-"*30)
print("Sequencia de Fibonacci")
print("-"*30)
num = int(input("Quantos termos vc queer mostrar? "))
t1 = 0
t2 = 1

print("~"*30)
print("{} → {}".format(t1, t2), end="")

count = 3

while count <= num:
    t3 = t1 + t2
    count += 1
    print(" → {}".format(t3), end="")
    t1 = t2
    t2 = t3