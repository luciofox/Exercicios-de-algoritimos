n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite a seguir o próximo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# "Nº" em ":. nº" é a quantidade de números (nº) que será visível em "Divisão";
# Logo, a lógica é: se for "{:.3f}" aparecerá 3 casas, mas se for "{:.2f}" já será 2 casas.

# "\n" é o comando para quebrar linha, sem a necessidade de novos "print()"s.

# ", end= ' ' " é o comando para juntar as linhas quebradas em "print()"s.
# Note que se pôr ">>>" em ", end= ' ' " (isso é:, end= ' >>> ') temos como resultado:
# um símbolo que representa o vazio que tinha até então; Até então, agora é: >>>

print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end= ' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))
