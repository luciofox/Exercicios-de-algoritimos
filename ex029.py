'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'A velocidade atual do seu carro é {velocidade}m/h, assim sendo, você foi mutado, pois ultrapassou 80Km/h!\nPortanto, recebeste uma multa de {multa} Reais.')
else:
    print('Que belo exemplo, a sua compostura no trânsito do Rio de Janeiro em!')
print('Tenha um bom dia. Dirija com segurança!')

'''
=== EX029 ===
from random import randint
from time import sleep
print('Seu carro passou no radar 🚗...')
sleep(2)
vel = randint(10,180)
if vel > 80:
    print('Você estava a {}Km/h e foi multado, o valor da multa é R${:.2f}'.format(vel, (vel-80)*7))
else:
    print('Sua velocidade é {}Km/h, continue respeitando os limites'.format(vel))

'''
