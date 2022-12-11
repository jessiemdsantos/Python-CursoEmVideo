'''Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento'''

print('')
print('='*20, 'AUMENTO DE SALÁRIO', '='*20)
print('')

s = float(input('Salário do funcionário: R$'))
aumento = s * 0.15
s += aumento

print(f'O salário do funcionário, com 15% de aumento, sobe para R${s:.2f}!')
