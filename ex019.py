import random
# NOTA 02: Porque "random"?

n1 = str(input('Digite o nome do aluno 01: '))
n2 = str(input('Digite o nome do aluno 02: '))
n3 = str(input('Digite o nome do aluno 03: '))
n4 = str(input('Digite o nome do aluno 04: '))
# NOTA 01: Por que temos aqui "str()"? R.: Porque é o "tipo primitivo" em TEXTO.

lista = [n1, n2, n3, n4]
# Comentário do prof.: P/ Python, uma lista, DEVE ficar dentro de concheites; Isso é: "[]"!

escolhido = random.choice(lista)
print('*' * 20)
print('O aluno escolhido foi, você: {}'.format(escolhido))
print('*' * 20)