''' Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''
produto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
           'Estojo', 25.00, 'Mochila', 120.00, 'Livro', 40.00,
           'Canetinha', 28.90, 'Régua', 12.50)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for i in range(0, len(produto)):
    if i % 2 ==0:
        print(f'{produto[i]:.<30}', end=' ')
    else:
        print(f'R$ {produto[i]:>6.2f}')
print('=' * 40)
