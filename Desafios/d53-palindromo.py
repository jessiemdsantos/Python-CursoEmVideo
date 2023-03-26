'''Crie um programa que leia uma frase qualquer e diga se ela é
um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).upper().strip()
div = frase.split()
junto = ''.join(div)
inverso = junto[::-1]
if inverso == junto:
    print(f'a frase "{frase}" é um palíndromo!')
else:
    print(f'a frase "{frase}" NÃO é um palíndromo!')

