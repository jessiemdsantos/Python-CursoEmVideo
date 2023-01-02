''' Escreva um programa que leia dois números inteiros e compare-os.
Mostre na tela uma mensagem dizendo se o primeiro valor é maior, se segundo valor
é maior ou se não existe valor maior e os dois são iguais '''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
    