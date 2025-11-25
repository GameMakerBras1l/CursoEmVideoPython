termo = int(input("Digite o primeiro termo: "))

razao = int(input("Agora digite a razão: "))

tg = 0

x = 1

while x <= 10:
    
    tg = termo + (x - 1)*razao

    print(tg, end= " -> ")

    x = x + 1

print("Codigo terminado")