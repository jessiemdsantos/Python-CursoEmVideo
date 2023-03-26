'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

n = int(input('Digite um número: '))
f = 1
print(f'{n}! = ', end='')
while n > 0:
    print(f' {n} ', end='')
    if n > 1:
        print('x', end='')
    else:
        print(' = ', end='')
    f *= n
    n = n - 1
print(f)



