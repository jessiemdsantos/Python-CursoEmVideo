'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais,
ISÓSCELES: dois lados iguais, um diferente e ESCALENO: todos os lados diferentes'''
print('')
print('='*20, 'Analisando Triângulos', '='*20)
print('')

a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Estas retas formam um triângulo EQUILÁTERO!')
    elif a == b != c or a == c != b or b == c != a:
        print('Estas retas formam um triângulo ISÓSCELES!')
    else:
        print('Estas retas formam um triângulo ESCALENO!')
else:
    print('Estas retas NÃO formam um triângulo!')