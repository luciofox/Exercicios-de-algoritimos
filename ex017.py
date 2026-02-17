'''
# ESSA É A MANEIRA MATEMÁTICA:

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))


# A SEGUIR, COM IMPORTAÇÃO DA CLASS MATH (isso é, nativo!):

import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Catego Adjacente: '))
hi = math.hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}.'.format(hi))

'''
# A SEGUIR, COM REFERÊNCIA DA ESPECIALIDADE EM CLASS MATH (isso é, nativo!):

from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjancete'))
hi = hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}.'.format(hi))
