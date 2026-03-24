'''Gabriel Henrique Pereira de Oliveira'''
print('-' * 20)

nome = str(input('Digite seu nome completo: ')).strip().lower()

print('-' * 20)

lista = nome.split()
print(f'Seu 1º nome é {lista[0].capitalize()}.')
# Está dando erro p/ mim este modo que o prof. passou:
print('Seu último nome é {}.'.format(nome[len(lista)-1].capitalize()))


print('-' * 20)

print(f'Seu primeiro nome é {lista[0].capitalize()} e seu último nome é {lista[-1].capitalize()}')

print('-' * 20)
# O Split[-1] já resolve o caso, simplificando sem precisar usar o len.
print('Seu primeiro nomé é: {}'.format(nome.split()[0].capitalize()))
print('Seu último nomé é: {}'.format(nome.split()[-1].capitalize()))
print('-' * 20)
