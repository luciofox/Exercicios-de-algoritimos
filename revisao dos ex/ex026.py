from shlex import split

frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece {} na frase.'.format(frase.count('a')))
print('A 1ª letra A aparece na posição {} desta frase.'.format(frase.find('a')+1))
# Olha a dica do +1 e p/ que serve; isso é, a lógica de programação!
print('A última letra A aparece na posição {} desta frase.'.format(frase.rfind('a')+1))
