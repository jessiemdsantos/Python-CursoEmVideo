'''Escreva um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido
pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu'''
from random import randint
from time import sleep

computador = randint(0, 5)

print('')
print('='*20,'VAMOS BRINCAR?' ,'='*20)
print('')
print('Adivinhe que número estou pensando...')
usuario = int(input('Escolha um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if computador == usuario:
    print(f'Arrasou! Eu pensei exatamente no número {computador}!')
else:
    print(f'Vish, você errou! Escolhi o número {computador}... Mais sorte da próxima vez!')