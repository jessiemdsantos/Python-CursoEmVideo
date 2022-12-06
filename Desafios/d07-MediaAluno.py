''' Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média '''

nome = input('Digite o nome do(a) aluno(a): ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2
print()
print('--------------------------------')
print('Aluno(a): ', nome)
print('Média do semestre: ', format(media))
print('--------------------------------')