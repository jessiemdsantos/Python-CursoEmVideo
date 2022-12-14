''' Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas, minúsculas, quantas letras ao
todo (sem espaço) e quantas letras tem o primeiro nome '''

nome = str(input('Digite seu nome completo: '))
print()
print('='*80)
print()
print(f'Seu nome, apenas em LETRAS MAIÚSCULAS: {nome.upper()}!')
print(f'Seu nome, apenas em letras minúsculas: {nome.lower()}!')
lista = nome.split()
junto = ''.join(lista)
print(f'Seu nome tem: {len(junto)} letras ao todo!')
print(f'Seu primeiro nome tem {len(lista[0])} letras!')
print()
print('='*80)
print()


