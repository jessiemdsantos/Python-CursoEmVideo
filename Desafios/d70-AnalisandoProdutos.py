'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final,
mostre: qual é o total gasto na compra. Quantos produtos custam mais de R$1000.
Qual é o nome do produto mais barato.'''
total = maisMil = menor = c = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('PREÇO: R$'))
    c += 1
    total += preco
    if preco > 1000:
        maisMil += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if opcao == 'N':
        print('')
        print('Finalizando...')
        print('')
        print('='*50)
        break
print(f'Total da compra: R${total:.2f}')
print(f'Sua compra teve {maisMil} produtos que custam mais de R$1.000')
print(f'O produto mais barato foi {barato}, que custa R${menor:.2f}.')


