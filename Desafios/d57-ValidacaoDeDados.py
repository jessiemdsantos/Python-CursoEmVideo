'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
 ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor
 correto.'''
sexo = str(input('Informe seu sexo [F/M]: ')).upper().strip()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dado invalido. Por favor, informe seu sexo [F/M]: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')