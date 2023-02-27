'''A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR,
Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER'''

from datetime import date
print('')
print('='*20, 'Categoria do Atleta', '='*20)
print('')
ano = int(input('Ano de nascimento? '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos. \nCategoria: MIRIM!')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. \nCategoria: INFANTIL!')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. \nCategoria: JÚNIOR!')
elif idade <= 25:
    print(f'O atleta tem {idade} anos. \nCategoria: SÊNIOR!')
else:
    print(f'O atleta tem {idade} anos. \nCategoria: MASTER!')
