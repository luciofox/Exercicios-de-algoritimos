'''
frase = "Gato"

frase = frase.replace('G', 'M')
print(frase) # Saída: Mato
'''

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2)/2
print('*' * 20)
print(f'A sua média foi {m:.1f}')
print('*' * 20)
if m >= 6.0:
    print('Sua nota boa; Parabens!')
else: # Nota A: Você estava achando que deveria por aqui "m < 6.0", mas não precisa por; somente "else:".
    print('Precisa melhorar!')
print('*' * 20)
print('Parabéns!' if m >=6 else 'ESTUDE MAIS!')
# Nota B: Exemplo de tudo numa linha só; Em um mesmo comando!
# Nota C: Chamamos isso de "condição simplificada". Isso é diferente de "condições compostas".
print('*' * 20)
