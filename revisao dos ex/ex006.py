'''
Desafio 006 - Dobro, Triplo e Raiz Quadrada
Crie um algaritmo que leia um nº e mostre o seu dobro, triplo e raiz quadrada.
'''

valor = int(input('Digite um nº e saiba o seu: dobro, triplo e raiz quadrada: '))

dobro = valor * 2
triplo = valor * 3
raizQuadrada = valor ** 2
# [dificuldade!] Nota¹: Para calcular a raiz Quadrada de um valor em Python, devemos:

print('Sendo o resultado do seu dobro {}, triplo {} e a raiz quadrada sendo {}'.format(dobro, triplo, raizQuadrada))
