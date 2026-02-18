'''
Título do material: Exercício Python #022 - Analisador de Textos

Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao TO-DO; Sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite seu nome completo: ')).strip()
# Lembre-se sempre da função ".strip()"
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper())) # ING é 'upper'
print('Seu nome em minúsculas é {}.'.format(nome.lower())) # ING é 'lower'
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
# CUIDADO! Antes estava ".format(len(nome)))", porém dava erro de LETRAS + ESPAÇO
# Não há mais erro ao aplicar a lógica do "-nome.count(' ')"! Veja ' '(espaço) - em 'nome'
# Em ING 'len' significa ''
# Lembre-se sempre da função ".strip()"!? Ajuda muito agora; mais ainda há mais!

# print('Seu 1º nome tem {} letras.'.format(nome.find(' ')))
# NÃO ENTENDI O DE CIMA

separa = nome.split() # variável_nova (separa) + objeto (nome) + .split()
# E, ".split()" é
print('Seu 1º nome é "{}", e ele tem {} letras.'.format(separa[0], len(separa[0])))
# "len(separa[0])" É 'len()' de 'separa'; Mas por que "0" (em [0])?
# ESTA OUTRA MANEIRA (até mais otimizado!); MAS NÃO ENTENDI por completo!
