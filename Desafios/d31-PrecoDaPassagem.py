'''Desenvolva um programa que pergunte a distãncia de
uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM
para viagens de até 200KM e R$0,45 para viagens mais longas'''

print()
print('='*20, 'Valor da Passagem', '='*20)
print()
distancia = float(input('Qual a distância, em KM, da sua viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'O valor da passagem fica R${valor:.2f}')
print('Boa viagem!!!')
