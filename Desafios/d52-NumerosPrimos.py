'''Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo.'''
div = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', c, '\033[m', end='')
        div += 1
    else:
        print('\033[31m', c, '\033[m', end='')
if div == 2:
    print(f'\n{n} é um número primo!')
else:
    print(f'\n{n} NÃO é um número primo!')
