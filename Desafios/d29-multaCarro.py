'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite'''

print()
print('='*20, 'LIMITE DE VELOCIDADE', '='*20)
print()

velocidade = float(input('Quantos Km/h estava o veículo? '))
if velocidade <= 80:
    print(f'Voce está dentro do limite. Continue assim!')
else:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou {velocidade - 80:.0f} Km/h do limite permitido '
          f'e está sendo multado!\n'
          f'O valor total da multa é R${multa:.2f}.')
