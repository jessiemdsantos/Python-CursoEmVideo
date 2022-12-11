'''Faça um programa que leia um ângulo qualquer e mostre na ela o valor
 do seno, cosseno e a tangente desse ângulo. (Precisa convernter
 em radiano, usando o radians na biblioteca math)'''
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ãngulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ãngulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ãngulo de {angulo} tem a TANGENTE de {tangente:.2f}')