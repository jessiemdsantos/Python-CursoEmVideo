'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'A pessoa mais pesada pesa {maior}Kg')
print(f'A pessoa mais leve pesa {menor}kg')


