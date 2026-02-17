'''
# [MEU ERRO] 1ª tentativa!

# ERREI!! Temos o dever e a responsabilidade de identificar meus erros e fraquezas amadoras. Em prol do aprendizado, profissionalismo e domínimo desta ferramenta de programação. Foi a 1ª vez que fiz essa espécie de exercício. Abaixo está como eu tentei:

import math
ang = float(input('Digite o valor de um ângulo qualquer, e assim, vai ter na tela o valor do seno, cosseno e tangente desse ângulo. Digite o valor do ângulo aqui: '))
seno = math.sin(ang)
cosseno = math.cos(ang)
tangente = math.tan(ang)

print('-' * 12)
print('O seno deste ângulo de {:.2f} é {:.2f}.'.format(ang, seno))
print('O cosseno deste ângulo de {:.2f} é {:.2f}.'.format(ang, cosseno))
print('A tangênte deste ângulo de {:.2f} é {:.2f}.'.format(ang, tangente))
print('-' * 12)
'''
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
# Comentário do prof.: Colocando-se assim "math.sin(math.radians())" nada impede de alinhar uma chamada em outra!
print('--' * 6)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
print('-' * 12)
