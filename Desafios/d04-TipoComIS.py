'''Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.'''

algo = input('Digite algo: ')

print('É alfanumérico?',format(algo.isalnum()))
print('É alfabético?',format(algo.isalpha()))
print('É decimal?',format(algo.isdecimal()))
print('É número?',format(algo.isnumeric()))
print('É printável?',format(algo.isprintable()))
print('Está em letras maiusculas?',format(algo.isupper()))
print('Está em letras minúsculas?', format(algo.islower()))
print('Só tem espaços?',format(algo.isspace()))
print('Está na tabela ascii?',format(algo.isascii()))
print('Está capitalizada?', format(algo.istitle()))