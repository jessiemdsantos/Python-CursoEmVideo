'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores. '''

continua = 'S'
soma = cont = maior = menor = 0
while continua == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continua = str(input('Quer continuar [S/N]? ')).upper().strip()
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media}')
print(f'O maior número foi {maior} e o menor número foi {menor}')
