''''responda ao usuário, pelo seu NOME'''
print('Olá! Bem-vindo. Como posso te ajudar? Diga-me seu nome: ')

nome = input()
print('Olá. Prazer em ter você aqui conosco, {}.'.format(nome))

cenario1 = input('Então... Vamos cuidar de X!')
cenario2 = input('Aguarde um instante. Estamos te direcionando.')

print('Por favor, digite {} para resolver X, ou, digite {} para falar com um de nossos atendentes. Agradecemos; Desde já, {}.'.format(cenario1, cenario2, nome))