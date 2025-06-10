n = float(input('Digite uma distancia em metros: '))

print('A medida de \033[32m{}\033[m corresponde a'.format(n))

print(n/1000,'km')
print(n/100,'hm')
print(n/10,'dam')
print(int(n*10),'dm')
print(int(n*100),'cm')
print(int(n*1000),'mm')