import math

g = 9.81

print("Calcular o alcance de um projétil")

h = float(input("Informar altura em relação ao solo: "))

v = float(input("Infomar velociade inicial em m/s: "))

ang = float(input("Informar angulo de lançamento em graus: "))


rad = math.radians(ang)

vx = v * math.cos(rad)

vy = v * math.sin(rad)


a = -g / 2
b = vy
c = h


delta = b**2 - 4*a*c

t1 = (-b + math.sqrt(delta)) / (2*a)
t2 = (-b - math.sqrt(delta)) / (2*a)

tempo = max(t1, t2)

distancia = vx * tempo

print(f"O projétil atinge o solo a {distancia:.2f} metros")