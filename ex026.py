'''
Exercício Python #026 - Primeira e última ocorrência de uma string

*Desafio*: Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase: ')).upper().strip() #NOTA: ".upper().strip()"; Isso é: .upper() + .strip()
# Comment¹: 1º precisamos ter a frase.
# Comment²: Vimos como vale a pena obtê-la em "str()". [DÚVIDA:] Mas porquê? Eu não entendi!

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A')))
# Comment³: É muito importante vc por ".upper()", pois assim, joga e TRANSFORMA tudo em maiúsculo!

print('A 1ª vez que a letra "a" apareceu na posição {}.'.format(frase.find('A')+1)) # NOTA: Veja o nº1!
# 4º Comment: "posição 0" fica esquesito aos olhos do usuário; Assim sendo, foi de ".find('A')" p/ ".find('A')+1".

print('A última letra "a" apareceu na posição {}.'.format(frase.rfind('A')+1))
# 5º Comment: O quê é 'r' em "rfind"? Signifca, começar a procurar do lado direito (ING: right)
