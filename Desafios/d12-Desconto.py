'''Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço com 5% de desconto'''
print('')
print('='*20, 'Super Promoção', '='*20)
print('')

produto = float(input('Valor do produto: R$'))
desconto = produto * 0.05
produto -= desconto
print(f'O valor do produto com 5% de descontro fica por R${produto:.2f}!')