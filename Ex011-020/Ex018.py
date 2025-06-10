import math
from idlelib.help import copy_strip

an = int(input('Digite um angulo: '))

rad = math.radians(an)

s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

print('O seno é \033[32m{:.2f}\033[m'.format(s))
print('O cosseno é \033[32m{:.2f}\033[m'.format(c))
print('A tangente é \033[32m{:.2f}\033[m'.format(t))