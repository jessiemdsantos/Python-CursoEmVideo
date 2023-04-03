'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
(termo, pulando a razão)'''
print('')
print('='*20, 'PROGRESSÃO ARITMÉTICA', '='*20)
print('')
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(numero, end=' -> ')
cont = 1
while cont < 10:
    termo = numero + razao
    numero = termo
    print(termo, end=' -> ')
    cont += 1
print('FIM')
