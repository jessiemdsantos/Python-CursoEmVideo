''' Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).'''
from time import sleep
num = int(input('Digite um número (ou 999 para encerrar): '))
soma = 0
cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (ou 999 para encerrar): '))
print('Encerrando...')
sleep(1)
print(f'Você digitou {cont} números e o total da soma entre eles é {soma}')
