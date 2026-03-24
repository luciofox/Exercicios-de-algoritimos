'''
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from time import sleep
from datetime import date
ano = int(input('Qual ano em mente quer analisar se é BISSEXTO?! Só 1 segundo!\nSe quiser saber se o ano atual é, basta digitar o nº "0".\nDigite o ano ou o nº" 0": '))
# Segundo o prof. é int() pq ninguém vai ler "meio ano". Me pergunto se em "lógica de programação" há casos...
print('Só um segundo!') # coloque sempre em cima do código "sleep()", senão só aparecerá depois do time configurado!
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é!")
else:
    print(f'O ano {ano} não é!')
