'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser
que quer mostrar 0 termos. '''
from time import sleep
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = numero
cont = 1
ultimo = 10
while cont <= ultimo:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
    if cont > ultimo:
        mais = int(input('Pausa\n'
                  'Quantos termos a mais você quer mostrar? '))
        if mais != 0:
            ultimo += mais
        else:
            print('Finalizando...')
sleep(1)
print(f'Acabou! Foram mostrados {ultimo} termos. Volte sempre! ')


