'''Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triangulo retangulo calcule e mostre o comprimento
da hipotenusa. a² + b² = c²'''

'''from math import sqrt, pow
a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))

co = pow(a, 2)
ca = pow(b, 2)
c = (co + ca)
hip = sqrt(c)
print(f'O comprimento da hipotenusa cujo o cateto oposto é {a:.0f} e o cateto '
      f'adjacente é {b} é {hip}')'''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print(f'O comprimento da hipotenusa cujo o cateto oposto é {co} e o cateto '
      f'adjacente é {ca} é igual a {hip:.2f}')