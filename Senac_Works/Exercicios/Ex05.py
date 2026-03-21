import math

num = float(input("Digite um número entre 0 ha 360: "))

while num < 0 or num > 360:

    num = float(input("Maior que 360 ou Menor que 0 digite outro número: "))


rad = (num * math.pi)/180

print(f"O radiano do numero digitado é {rad:.2f}")