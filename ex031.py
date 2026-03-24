'''
Há 2 maneiras!
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.
'''

from time import sleep

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {distancia}km.')
print('Processando o valor!\nAgradecemos por confiar em nossa empresa. :D')
sleep(5)

print('-=-' * 20)

# Modo A:
print('Modo A:')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}.')

print('-=-' * 20)

# Modo B:
print('Modo B:')
modoB = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${modoB:.2f}.')
