from shlex import split

primeiro = str(input('Digite seu nome completo: '))
nome = primeiro.strip()

print('Há {} letras ao todo. Mas sem considerar o espaço!'.format(len(nome) - nome.count(' ')))
print('Seu nome em letra maiúsculo é: "{}"'.format(nome.upper()))
print(f'Seu nome em letra minúsculo é: "{nome.lower()}".')
#print('O seu 1º nome tem {} letras ao total'.format(primeiro.find(' ')))
lista = primeiro.split()
print('Seu 1º nome é {}, e ele tem {} letras.'.format(lista[0], len(lista[0])))
