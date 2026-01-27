"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
 sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""
kmPercorridos = float(input("Quantos km foram percorridos por seu carro alugado? "))
diasAlugados = float(input('Por quantos dias seu carro foi alugado? '))

precoDiaria = 60.0
precoPorKm = 0.15



precoTotalKm = kmPercorridos * precoPorKm
precoDiarias = diasAlugados * precoDiaria

valorTotal = precoDiarias + precoTotalKm

print("Mediante ao total de {} dias alugados, e por {} Km pecorridos, o valor total é {} Reais".format(diasAlugados, kmPercorridos, valorTotal))