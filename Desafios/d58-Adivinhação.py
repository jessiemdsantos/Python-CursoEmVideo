'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('')
print('='*20, 'JOGO DE ADIVINHAÇÃO', '='*20)
print('')
computador = randint(0, 10)
usuário = int(input('Dê 0 a 10, qual número estou pensando? '))
s = 1
while usuário != computador:
    if computador > usuário:
        usuário = int(input('ERROU! É mais...Tente de novo!\nQual número estou pensando? '))
    elif computador < usuário:
        usuário = int(input('ERROU! É menos...Tente de novo!\nQual número estou pensando? '))
    s += 1
print(f'Parabéns! Você acertou! Pensei no número {computador}!\n'
      f'Você acertou na {s}ª tentativa!')
