'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
from time import sleep
print('')
print('=' * 10, 'CAIXA ELETRÔNICO VIRTUAL', '=' * 10)
print('')
saque = int(input('Qual valor deseja sacar? R$'))
print('\nExecutando saque...')
sleep(1)
print('=' * 45)
while True:
    if saque >= 50:
        cont50 = saque // 50
        print(f'Total de {cont50} cédulas de R$50')
        saque -= (cont50 * 50)
    if saque >= 20:
        cont20 = saque // 20
        print(f'Total de {cont20} cédulas de R$20')
        saque -= (cont20 * 20)
    if saque >= 10:
        cont10 = saque // 10
        print(f'total de {cont10} cédulas de R$10')
        saque -= (cont10 * 10)
    if saque >= 1:
        cont1 = saque // 1
        print(f'Total de {cont1} cédulas de R$1')
        saque -= (cont1 * 1)
    if saque == 0:
        break
print('=' * 45)
print('Agradecemos a preferência! Volte sempre!')
