'''
**Título do material:** Exercício Python 023 - Separando dígitos de um número

*Desafio*: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# VERSÃO 1:

num = int(input('Informe um nº: '))
n = str(num)
print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

# [DÚVIDA!] Por quê usa-se "[número]"?

'''
# VERSÃO 2:

num = int(input('Informe um nº: '))
u = num // 1 % 10
# NOTA: O prof. recomenda testar fazer antes de por "% 10" e comparar; vai notar o que há de legal!
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
