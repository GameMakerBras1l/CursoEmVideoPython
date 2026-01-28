sexo = ""

while (sexo != "M") and (sexo != "F"):
    sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]

    if sexo == "M":
        print("Seu sexo é o masculino")
    
    elif sexo == "F":
        print("Seu sexo é o feminino")

    else:
        print("Você não digitou uma letra solicitada, repita o processo")
        print("")