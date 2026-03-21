import math

num = float(input("Digite um radiano: "))

while num < 0 or num > 2 * math.pi:
    num = float(input("Não é um numero apropriado, digite outro: "))

grau = (num * 180)/math.pi

print(f"Em graus fica {grau:.2f}")