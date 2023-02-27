'''Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''
s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
print(f'A soma dos números ímpares que são multiplos de 3, entre 1 a 500 é: {s}')

