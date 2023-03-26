'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. (termo, pulando a razão)'''

num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = num + (10 - 1) * razao
print('Os 10 primeiros termos dessa PA é: ')
for c in range(num, termo + razao, razao):
    print(c)
print('Fim')

