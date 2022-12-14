'''Crie um programa que leia o nome de uma pessoa e diga se ela
tem o nome 'SILVA' '''

nome = str(input('Digite o nome completo: ')).strip()

if 'SILVA' in nome.upper():
    print('Possui "Silva" no nome.')
else:
    print('Não possui "Silva" no nome.')