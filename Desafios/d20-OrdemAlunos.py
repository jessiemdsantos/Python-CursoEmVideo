'''O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada (shuffle é usado
para embaralhar)'''

from random import shuffle

a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'Ordem de apresentação: {lista}')