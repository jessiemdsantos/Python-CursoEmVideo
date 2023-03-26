'''Crie um programa que leia dois valores e mostre um menu na tela com as
opções: somar, multiplicar, ver maior, novos números, sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('Muito bem, qual operação deseja realizar? ')
print('''
[1] SOMAR
[2] MULTIPLICAR
[3] VER MAIOR NÚMERO
[4] ESCOLHER NOVOS NÚMEROS
[5] SAIR''')
opção = int(input('Sua opção: '))
while opção != 5:
    if opção == 1:
        print(f'{n1} + {n2} = {n1+n2} ')
        opção = int(input('Sua opção: '))
    elif opção == 2:
        print(f'{n1} x {n2} = {n1*n2} ')
        opção = int(input('Sua opção: '))
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            opção = int(input('Sua opção: '))
        elif n1 == n2:
            print(f'Não há maior, pois {n1} e {n2} são iguais!')
            opção = int(input('Sua opção: '))
        else:
            print(f'{n2} é maior que {n1}')
            opção = int(input('Sua opção: '))
    elif opção == 4:
        n1 = int(input('Novo primeiro número: '))
        n2 = int(input('Novo segundo número: '))
        opção = int(input('Sua opção: '))
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
        opção = int(input('Sua opção: '))
print('Finalizando...')
sleep(1)
print('Fim do programa')
