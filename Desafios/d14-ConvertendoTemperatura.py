'''Escreva um programa que converta uma temperatura digitando
em graus Celsius e converta para graus Fahrenheit.'''

# fórmula = (ºC * 1,8) + 32
C = float(input('Digite a temperatura em ºC: '))
F = C * 1.8 + 32
print(f'{C}ºC convertido para Fahrenheit fica {F:.1f}ºF')
