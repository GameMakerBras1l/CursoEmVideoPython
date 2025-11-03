somaidade = 0
mediaidade = 0
maioridade = 0
menoridade = 0
nomevelho = ""
for p in range (1, 5):
    print(f"-----{p}* PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridade:
        maioridade = idade
        nomevelho = nome

    if sexo in "Ff" and idade < 20:
        menoridade += 1

mediaidade = somaidade/4
print(f"A Media de Idade do Grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridade} e seu nome é {nomevelho}.")
print(f"O número de mulheres com menos de 20 anos são {menoridade}")