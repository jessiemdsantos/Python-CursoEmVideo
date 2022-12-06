'''Crie un algoritmo que leia um número
e mostre o seu dobro, triplo e sua raiz quadrada '''

num = int(input('Digite um número: '))
d = num * 2
t = num * 3
rq = num ** (1 / 2)

print(f'O número escolhido foi o {num}, seu dobro é {d}, o seu triplo é {t} e sua raíz quadrada é {rq:.2f}')