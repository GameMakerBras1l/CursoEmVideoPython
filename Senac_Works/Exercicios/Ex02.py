x = y = 10
x = x + 1
z = x
x = -x
y = y + 1
x = x + y - z
z = z - 1

print(f"X = {x}")
print("")

print(f"Y = {y}")
print("")

print(f"Z = {z}")