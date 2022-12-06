''' Escreva um programa que leia um valor, em metros,
e o exiba convertido em centimetros e milimetros '''

print('')
print('='*20,'Conversor de Medidas', '='*20)
print('')
valor = float(input('Digite o valor, em metros: '))

c = valor * 100
m = valor * 1000

print(f'Valor em metros {valor}.')
print(f'Convertido: {c:.2f} centímetros e {m:.2f} milímetros.')

