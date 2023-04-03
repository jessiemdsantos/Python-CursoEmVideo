'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.'''
from random import randint
print('')
print('='*20, 'VAMOS JOGAR PAR OU ÍMPAR?', '='*20)
print('')
computador = randint(0, 10)
usuario = int(input('Diga um valor (entre 0 e 10): '))
opcao = str(input('Ímpar ou Par [I/P]? ')).upper().strip()
c = 0
while True:
    if opcao == 'P':
        if (usuario + computador) % 2 != 0:
            print(f'O computador jogou {computador} e você {usuario}. O total é {usuario + computador}, que dá ÍMPAR!')
            print('-' * 30)
            break
        else:
            c += 1
            print(f'Você ganhou! Computador jogou {computador} e você jogou {usuario}. O total é {usuario + computador}, que dá PAR!')
            print('Vamos jogar novamente...')
            print('-' * 30)
            computador = randint(0, 10)
            usuario = int(input('Diga um valor (entre 0 e 10): '))
            opcao = str(input('Ímpar ou Par [I/P]? ')).upper().strip()
    elif opcao == 'I':
        if (usuario + computador) % 2 == 0:
            print(f'O computador jogou {computador} e você {usuario}. O total é {usuario + computador}, que dá PAR!')
            print('-' * 30)
            break
        else:
            c += 1
            print(f'Você ganhou! Computador jogou {computador} e você jogou {usuario}. O total é {usuario + computador}, que dá ÍMPAR!')
            print('Vamos jogar novamente...')
            print('-' * 30)
            computador = randint(0, 10)
            usuario = int(input('Diga um valor (entre 0 e 10): '))
            opcao = str(input('Ímpar ou Par [I/P]? ')).upper().strip()
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente...')
        opcao = str(input('Ímpar ou Par [I/P]? ')).upper().strip()
print('Que Pena, você perdeu!')
print('=' * 30)
print(f'GAME OVER! Você ganhou {c} vezes.')
