'''Faça um programa que leia um numero de 0 a 9999 e mostre na
tela cada um dos digitos separados'''

num = str(input('Digite um numero de até 4 digitos: '))

if len(num) == 4:
    print('Unidade:', num[3])
    print('Dezena:', num[2])
    print('Centena:', num[1])
    print('Milhar:', num[0])
elif len(num) == 3:
    print('Unidade:', num[2])
    print('Dezena:', num[1])
    print('Centena:', num[0])
elif len(num) == 2:
    print('Unidade:', num[1])
    print('Dezena:', num[0])
elif len(num) == 1:
    print('Unidade:', num[0])
else:
    print('ERRO: Número com mais de 4 digitos!')


