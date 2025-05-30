la = float(input('Digite a Largura da Parede: '))
al = float(input('Digite a Altura da Parede: '))

area = la*al

tinta = area/2

print('A dimensão da parede é de \033[32m{}x{}\033[m e sua área é de \033[32m{}m2,\033[m '
      'a quantidade de tinta necessaria para pintar a parede é de \033[32m{:.2f}L'.format(la,al,area,tinta))