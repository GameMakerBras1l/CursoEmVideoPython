total = int(input("Digite uma qauntidade de tempo em segundos: "))

horas = total // 3600

resto = total % 3600

minutos = resto // 60

segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")