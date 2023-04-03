''' Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 '''
anterior = 0
atual = 1
proximo = 0
cont = 0
n = int(input('Quantos termos você quer mostrar? '))
print(f'{anterior} -> {atual} ->', end=' ')
while cont < (n-2):
    proximo = anterior + atual
    print(proximo, end=' -> ')
    anterior = atual
    atual = proximo
    cont += 1
print('FIM')
