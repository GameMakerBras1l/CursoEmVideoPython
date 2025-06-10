n = input('Digite o seu nome completo: ').strip()
nome = n.split()

print('O seu primeiro nome é \033[32m{}\033[m'.format(nome[0]))
print('O seu ultimo nome é \033[32m{}^\033[m'.format(nome[len(nome)-1]))