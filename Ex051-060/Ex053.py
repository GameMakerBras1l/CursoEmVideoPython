frase = input("Escreva uma frase ser sem acento: ").split()

frase2 = "".join(frase)

frase3 = frase2[::-1]

if frase2 == frase3:
    print("Essa frase é um palíndromo")
else:
    print("Essa frase não é um palíndromo")