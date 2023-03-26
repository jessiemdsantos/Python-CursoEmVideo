'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos.'''
soma = 0
maisVelho = 0
qtdeMulheres = 0

for c in range(1, 5):
    print(f'=== {c}ª PESSOA ===')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    soma += idade
    if sexo == 'F' and idade < 20:
        qtdeMulheres += 1
    if sexo == 'M':
        if c == 1:
            maisVelho = idade
            nomeMaisVelho = nome
        else:
            if idade > maisVelho:
                maisVelho = idade
                nomeMaisVelho = nome
media = soma / 4
print(f'A média da idade do grupo é {media} anos')
print(f'O nome do homem mais velho é {nomeMaisVelho} e ele tem {maisVelho} anos')
print(f'Há {qtdeMulheres} mulher(es) com menos de 20 anos')
