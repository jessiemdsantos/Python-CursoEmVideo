'''Faça um programa que leia um frase pelo teclado e mostre:
- quantas vezes aparece a letra A;
- em que posição ela aparece a primeira vez;
- em que posição ela aparece a ultima vez; '''

frase = str(input('Digite uma frase: ')).strip()

print(f'A letra "A" aparece {frase.upper().count("A")} vezes nesta frase.')
print(f'A letra "A" aparece pela primeira vez na posição {frase.upper().find("A")+1}.')
print(f'A letra "A" aparece pela última vez na posição {frase.upper().rfind("A")+1}.')