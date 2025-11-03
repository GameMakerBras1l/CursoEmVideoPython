t = int(input("Digite o primeiro termo: "))

r = int(input("Agora digite a razão: "))

tg = 0


print("Os 10 primeiros números dessa PA(progreção aritimetica) são")

for c in range (1, 10+1):
    tg = t + (c - 1)*r
    print(tg, end= " -> ")

print("Acabou a PA")