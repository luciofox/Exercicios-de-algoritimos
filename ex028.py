'''
Exercício Python 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep # Comentário: faz com que o programa demore um tempo configurado para responder.

computador = randint(0, 5) # Comentário do prof.: Faz o computador "pensar".
#Exemplo: print(f'Pense no número {computador}.')
print('-=-' * 20)
print('Pense em um nº entre 0 a 5!')
print('-=-' * 20)
jogador = int(input('Escreva a seguir, o nº que você pensou: '))
print('-=-' * 20)
print('Processando...\nCanalize sua sorte!')
sleep(5)
print('-=-' * 20)

if jogador == computador:
    print(f'PARABÉNS! Você ganhou o sorteio.\nFoi o nº {computador} o nº sorteado.')
else:
    print(f'Você disse "{jogador}"?! SINTO MUITO :(\nNão ganhou, pois o nº sorteado foi {computador}!')
