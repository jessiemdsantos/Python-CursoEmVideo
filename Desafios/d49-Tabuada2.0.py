'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for.'''

n = int(input('Digite um número: '))
print('')
print('='*2, 'TABUADA', '='*2)
for c in range(0, 11):
    r = n * c
    print(f'{n} x {c:2} = {r:2}')