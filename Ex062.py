t = int(input("Digite o Termo: "))

r = int(input("Digite a Razão: "))

tg = 0

x = 0

c = "S"

while c == "S":
    tg = t + (x + 1)*r
    print(tg)

    x +=1

    c = input("Digite 'S' se deseja mais um termo: ").upper()


print("FIM DA PA")