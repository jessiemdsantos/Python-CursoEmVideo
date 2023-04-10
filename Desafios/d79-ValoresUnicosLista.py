'''Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''
from time import sleep
num = []
while True:
    n = int(input("Digite um valor: "))
    if n not in num:
        num.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper()
    if opcao == 'N':
        print('-' * 50)
        print('Finalizando...')
        sleep(1)
        print('CADASTRO FINALIZADO')
        print('-' * 50)
        break
num.sort()
print(f'Você digitou os valores {num}')