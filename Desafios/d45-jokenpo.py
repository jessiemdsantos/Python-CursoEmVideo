'''Crie um programa que faça o computador jogar Jokenpô com você.'''
print('')
print('='*20, 'VAMOS JOGAR JOKENPÔ?','='*20)
print('')
from random import randint
from time import sleep
computador = randint(1, 3)
print('''Qual a sua escolha? 
[1] - Pedra
[2] - Papel
[3] - Tesoura''')
opção = int(input('Sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
sleep(1)
if opção == 1 == computador:
    print('Você = Pedra X Computador = Pedra')
    print('Empatou!')
elif opção == 2 == computador:
    print('Você = Papel X Computador = Papel')
    print('Empatou!')
elif opção == 3 == computador:
    print('Você = Tesoura X Computador = Tesoura')
    print('Empatou!')
elif opção == 1 and computador == 2:
    print('Você = Pedra X Computador = Papel')
    print('Papel vence de Pedra, você perdeu!')
elif opção == 1 and computador == 3:
    print('Você = Pedra X Computador = Tesoura')
    print('Pedra vence de Tesoura, você ganhou!')
elif opção == 2 and computador == 1:
    print('Você = Papel X Computador = Pedra')
    print('Papel vence de Pedra, você ganhou!')
elif opção == 2 and computador == 3:
    print('Você = Papel X Computador = Tesoura')
    print('Tesoura vence de Papel, você perdeu!')
elif opção == 3 and computador == 1:
    print('Você = Tesoura X Computador = Pedra')
    print('Pedra vence de Tesoura, você perdeu!')
elif opção == 3 and computador == 2:
    print('Você = Tesoura X Computador = Papel')
    print('Tesoura vence de Papel, você ganhou!')
else:
    print('OPÇÃO INVALIDA!Tente novamente')