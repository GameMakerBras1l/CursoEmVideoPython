a = input('Digite algo: ')

print('Tipo primitivo: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Esta em maisuculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())