''' Faça um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%, para os inferiores ou iguais,
o aumento é 15%'''

salario = float(input('Salário do funcionário: R$ '))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
print(f'Salário antigo = R${salario:.2f} \nAumento = {aumento:.2f}'
          f' \nSalário atual = R${salario + aumento:.2f}')