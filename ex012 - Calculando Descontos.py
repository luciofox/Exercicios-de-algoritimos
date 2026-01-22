preco = float(input('Qual é o preço do produto? R$ '))

desconto = preco * 5 / 100
novo_preco = preco - desconto

print('O produto que custava R$ {:.2f}'.format(preco))
print('Na promoção com desconto de 5% vai custar R$ {:.2f}'.format(novo_preco))