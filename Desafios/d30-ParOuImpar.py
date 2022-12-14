'''Crie um programa que leia um número qualquer e mostre
na tela se ele é Par ou Ímpar'''

num = int(input('Escolha um número: '))
if num % 2 == 0:
    print(f'Vocé escolheu o número {num}, este número é PAR!')
else:
    print(f'Vocé escolheu o número {num}, este número é ÍMPAR!')