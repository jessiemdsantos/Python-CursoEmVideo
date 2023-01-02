''' Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triangulo'''

print()
print('='*20, 'Analisando Triângulos', '='*20)
print()

a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Estas retas formam um triângulo.')
else:
    print('Não formam um triângulo.')

