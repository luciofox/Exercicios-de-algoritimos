'''
Exercício Python 035:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Comentário da aula:
fazer e fez uma pesquisa Provavelmente você chegou a essa regra a regra diz o seguinte cada um desses segmentos tem que
ser menor do que a soma do comprimento dos outros dois então por exemplo ali ó o R1 tem que ser menor do que a soma dos
outros dois do que o R2 do que o R3 o R2 por exemplo que essa linha amarela ela não é menor do que o R1 mais o R3 Eles
não conseguem encostar lá em cima então é por isso que existe esse problema é por isso que os professores de
programação passam esse desafio.

'''

r1 = float(input("1º segmento: "))
r2 = float(input("2º segmento: "))
r3 = float(input("3º segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Infelizmente não dá.')
