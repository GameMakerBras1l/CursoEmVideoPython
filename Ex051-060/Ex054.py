from datetime import date
n = 0
a = date.today().year
a2 = 0

for c in range (0, 7):
    a2 = int(input("Digite o ano de nassimento de alguem: "))
    if (a - a2) >= 18:
        n = n + 1

print(f"Das 7 pessoas cujo o nome foi digitado {n} são maior de idade")