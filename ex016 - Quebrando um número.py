'''
Crie um programa que leia o número Real qualquer pelo teclado e mostre na a
sua porção inteira.

Ex.: Gigite 6.127
O número 6.127 tem a parte 6
'''

import math
num = float(input('Digite o número que você deseja ver a porção inteira: '))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))
