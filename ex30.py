'''
Exercício Python 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
from time import sleep

numero = int(input('Digite aqui o nº, para juntos analisarmos se é PAR ou ÍMPAR.\nDiga ele: '))
resultado = numero % 2

print('PROCESSANDO... 1 segundo!')
sleep(1)

if resultado == 0: # Eu estava esquecendo de que era "==" e não "="!
    print(f'O nº {numero} é PAR.')
else:
    print(f'O nº {numero} é ÍMPAR.')
