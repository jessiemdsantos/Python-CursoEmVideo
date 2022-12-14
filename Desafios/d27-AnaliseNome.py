'''faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o ultimo nome separadamente'''

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f'Pazer em te conhecer, {nome[0]}!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu ultimo nome é {nome[len(nome)-1]}.')
