''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada
 pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
 No final, mostre: quantas pessoas tem mais de 18 anos. Quantos homens foram
 cadastrados. Quantas mulheres tem menos de 20 anos.'''
from time import sleep
qtHomem = maior = qtMulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()
    if sexo == 'M':
        qtHomem += 1
    else:
        if idade < 20:
            qtMulher += 1
    if idade > 18:
        maior += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if opcao == 'N':
        print('-' * 50)
        print('Finalizando...')
        sleep(1)
        print('CADASTRO FINALIZADO')
        print('-' * 50)
        break
print(f'Foram cadastradas {maior} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {qtHomem} homens.')
print(f'Foram cadastradas {qtMulher} mulheres com menos de 20 anos.')

