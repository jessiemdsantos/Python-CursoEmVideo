''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto,
em até 2x no cartão: preço formal ou 3x ou mais no cartão: 20% de juros'''

compra = float(input('Valor da compra: R$'))
print('')
print('='*10, 'Selecione a forma de pagamento', '='*10)
print('[1] À vista no dinheiro ou PIX\n'
      '[2] À vista no cartão ou cheque\n'
      '[3] Parcelado em 2x no cartão\n'
      '[4] Parcelado em 3x ou mais no cartão ')
opção = int(input('Digite sua opção: '))
print(f'Total da compra = R${compra:.2f}')
if opção == 1:
    valor = compra - (compra * 0.10)
    print(f'Total à pagar = R${valor:.2f} (à vista com 10% de desconto). ')
elif opção == 2:
    valor = compra - (compra * 0.05)
    print(f'Total à pagar = R${valor:.2f} (à vista com 5% de desconto). ')
elif opção == 3:
    valor = compra / 2
    print(f'Total à pagar = 2x de R${valor:.2f}')
elif opção == 4:
    num = int(input('número de parcelas: '))
    juros = compra + (compra * 0.20)
    valor = juros / num
    print(f'Total à pagar = {num}x de R${valor:.2f}. O custo final ficara em R${juros:.2f} com juros. ')
else:
    print('OPÇÃO INVÁLIDA! Tente novamente!')
    