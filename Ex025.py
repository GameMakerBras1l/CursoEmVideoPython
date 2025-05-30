n = input('Digite o seu nome completo: ').strip()

print('Seu nome completo tem \033[32mMarcel\033[m? {}'.format('MARCEL' in n.upper()))