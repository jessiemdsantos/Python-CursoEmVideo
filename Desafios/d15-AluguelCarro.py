'''Escreva um programa que pergunte a quantidade de Km percorridos
 por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
 e R$0,15 por Km rodado.'''

print('')
print('='*20, 'ALUGUEL DE CARRO', '='*20)
print('')

Km = float(input('Quantos KM o carro percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preço = (Km * 0.15) + (dias * 60)
print(f'O valor a pagar pelo aluguel é: R${preço:.2f}')
