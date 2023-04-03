'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.'''
from time import sleep
while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor (ou numero negativo para encerrar)? '))
    print('-'*40)
    if num < 0:
        break
    for cont in range(0, 11):
        print(f'{num} x {cont:2} = {num * cont:2}')
print('Encerrando...')
sleep(1)
print('Encerrado! Volte sempre!')
