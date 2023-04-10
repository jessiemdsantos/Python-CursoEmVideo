'''Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
num = []
print('=' * 70)
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(num) == 0 or n > max(num):
        num.append(n)
        print('Valor adicionado na ultima posição da lista...')
    else:
        if n > min(num):
            if num[1] < n < num[2]:
                num.insert(2, n)
                print(f'Adicionado na posição {num.index(n)} da lista...')
            else:
                num.insert(num.index(min(num))+1, n)
                print(f'Adicionado na posição {num.index(n)} da lista...')
        else:
            num.insert(num.index(min(num)), n)
            print(f'Adicionado na posição {num.index(n)} da lista...')
print('=' * 70)
print(f'\nOs valores digitados, de forma ordenada, foram {num} ')


