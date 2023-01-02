''' Faça um programa que leia três numeros e mostre
qual é o maior e qual é o menor '''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print()
print(f'Você digitou os números {n1}, {n2} e {n3}.')
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'Maior = {n1} \nMenor = {n3}')
    else:
        print(f'Maior = {n1} \nMenor = {n2}')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'Maior = {n2} \nMenor = {n3}')
    else:
        print(f'Maior = {n2} \nMenor = {n1}')
else:
    if n2 > n1:
        print(f'Maior = {n3} \nMenor = {n1}')
    else:
        print(f'Maior = {n3} \nMenor = {n2}')

'''Forma bem mais simplificada:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
numeros = [n1, n2, n3]

print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor numero digitado foi {min(numeros)}') '''
