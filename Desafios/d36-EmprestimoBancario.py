''' Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. A prestação mensal não pode exceder
30% do salário ou então o empréstimo será negado. '''

print()
print('='*20, 'Empréstimo Bancário', '='*20)
print()
casa = float(input('Valor da casa? R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Em quantos anos vai pagar? '))

prestacao = casa/anos/12
if salario * 0.30 < prestacao:
    print(f'Sentimos muito, mas seu empréstimo foi negado!\n'
          f'Para pegar uma casa de {casa:.2f} em {anos}x a prestação seria de {prestacao:.2f}, excendendo os 30% do seu salário. ')
else:
    print(f'Parabéns! Seu emprestimo foi aprovado!\n'
          f'Você pagará {anos * 12}x de RS{prestacao:.2f}')

