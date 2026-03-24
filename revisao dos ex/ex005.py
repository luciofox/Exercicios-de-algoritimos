'''
Exercício Python #005 - Antecessor e Sucessor

Faça um programa que leia um nº inteiro e mostra na tela seu sucessor e seu antecessor.
'''

numero = int(input('Digite a seguir o valor o qual você deseja saber o seu sucessor e seu antecessor: '))
# Nota¹: int() é Valor Primitivo; Nota²: input() é o ouvido (canal de audição) da máquina/Python!

sucessor = numero + 1
antecessor = numero - 1
# Nota³: Aqui é uma simples lógica de somar ou diminuir pelo valor nº 1.

print('O resultado é: seu sucessor é {} e seu antecessor é {}.'.format(sucessor, antecessor))
