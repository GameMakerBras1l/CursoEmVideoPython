n = input('Digite o seu nome: ').strip()

print('A letra A aparece \033[32m{}\033[m vezes'.format(n.upper().count('A')))
print('A primeira na posição \033[32m{}\033[m'.format(n.upper().find('A')))
print('E a ultima na posição \033[32m{}\033[m'.format(n.upper().rfind('A')))