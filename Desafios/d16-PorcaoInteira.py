''' Crie um programa que leia um numero real qualquer e mostre
na tela sua porção inteira '''
# ex: 5.125 mostra 5

'''from math import floor
num = float(input('Digite um número: '))
inteiro = floor(num)
print(f'O número {num} tem a parte inteira {inteiro}')'''

from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')