'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo: IMC abaixo de 18,5: Abaixo do Peso,
Entre 18,5 e 25: Peso Ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade e Acima
de 40: Obesidade Mórbida'''
print('')
print('='*20, 'Calculadora IMC', '='*20)
print('')
altura = float(input('Digite sua altura(m): '))
peso = float(input('Digite seu peso(Kg): '))
imc = peso / (altura * altura)
print(f'O seu Índice de Massa Corporal é {imc:.1f}Kg/m²!')
if imc < 18.5:
    print(f'Você está ABAIXO DO PESO, precisa se alimentar melhor!')
elif imc < 25:
    print('Parabéns! Você está com o PESO IDEAL. Continue assim!')
elif imc < 30:
    print('Atenção! Você está com SOBREPESO, precisa se alimentar melhor!')
elif imc < 40:
    print('Cuidado! Você está com OBESIDADE, procure ajuda de um nutricionista! ')
else:
    print('Cuidado! Você está com OBESIDADE MÓRBIDA, procure ajuda de um nutricionista! ')


