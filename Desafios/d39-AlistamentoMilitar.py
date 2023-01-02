''' Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date
print()
print('='*20, 'Alistamento Militar', '='*20)
print()
print('''Digite a opção que corresponde ao seu sexo:
1 - Feminino
2 - Masculino''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('Você não precisa fazer alistamento militar obrigatório!')
elif opção == 2:
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    if idade > 18:
        print(f'O alistamento é com 18 anos, você passou {idade-18} ano(s) do prazo!')
    elif idade < 18:
        print(f'O alistamento é com 18 anos, faltam {18-idade} ano(s) para você se alistar!')
    else:
        print('Você completou 18 anos, está na hora de se alistar!')
else:
    print('Opção inválida! Tente novamente!')