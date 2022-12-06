''' Crie um programa que leia quanto a pessoa tem na carteira e mostra quantos dólares
ela pode comprar. Considerar dolar = 3.27 '''

real = float(input('Qual o valor que você tem na sua carteira: R$'))

dolar = 3.27
res = real/dolar

if res == 0.0:
    print('Oh! Com esse valor você não consegue comprar nenhum dólar!')
else:
    print(f'Com esse valor você consegue comprar ${res:.2f}.')