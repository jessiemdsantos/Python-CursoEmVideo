'''Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista. No final, mostre qual foi o maior e o menor valor digitado e
as suas respectivas posições na lista.'''
num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(num)
menor = min(num)
print('')
print('=-' * 35)
print(f'Você digitou os valores {num}')
print(f'O maior valor foi {maior} e ele foi digitado nas posições: ', end='')
for pos, i in enumerate(num):
    if maior == i:
        print(f'{pos}... ', end='')
print(f'\nO menor valor foi {menor} e ele foi digitado nas posições: ', end='')
for pos, i in enumerate(num):
    if menor == i:
        print(f'{pos}... ', end='')
print('')
print('=-' * 35)
