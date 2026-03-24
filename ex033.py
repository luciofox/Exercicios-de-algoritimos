'''
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))

# verificando quem é menor
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')
