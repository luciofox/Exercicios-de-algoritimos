from itertools import count
from shlex import split

nome = str(input('Digite o nome da cidade: ')).strip().capitalize()
print(nome[:5]) # tive dificuldade aqui! Enquanto que, acima fiz muito bem, usando : .strip().capitalize()
# veja o raciocínio lógico por trás de usar "print(nome[:5])" >> [:5] << Por que [:5]?!
