'''
**Título do material:** Exercício Python 023 - Separando dígitos de um número

*Desafio*: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# [DÚVIDA!] Por quê usa-se "[número]"?

'''
from itertools import count

# O prof. Guanabara ensina de 2 modos. Sendo eles: A) String; B) Matemática.

# --- A) String ----

num = int(input('Informe um número de 0 até 9999: '))
n = str(num)
# O método 'A) String', diferentemente do método 'B) Matemática', deve-se usar Milhar[3];
# Em 'A) String' deve-se por > ou = "1000", senão vai dar erro, pois tem que haver algo em Milhar[3]!


print('-' * 20)

print('# --- A) String ----')
print('Analisando o nº {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

print('-' * 20)
# --- B) Matemática ----

u = num // 1 % 10
d = num // 10 % 10
# Nota¹: o professor enfatiza você comparar por e tirar o '% 10', e observar o que pega e o que ou deixa!
# Continuação da Nota¹: exemplifica ele c/ '1234', onde quando:
# * está sem '% 10' aparece: 123, mas quando há '% 10' pega o dígito '3' de 1234.
# * Mais quando ele põem '% 100', ele vai pegar mais 2 dígitos (pega '23' de 1234).
c = num // 100 % 10
m = num // 1000 % 10
# Nota²: Veja o padrão. Você consegue 'fatiar' o nº, 'particionar' o nº, usando a matemática.

# Dúvida: Por que por 10? Eu pensei que seria: "c = num // 100 % 100" e "m = num // 1000 % 1000".

print('# --- B) Matemática ----')
print('Analisando o nº {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('-' * 20)

