'''Faça um programa que leia um ano qualquer e mostre
se ele é ou não um ano bissexto.'''
from datetime import date
ano = int(input('Digite um ano qualquer ou digite 0 pro ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} É ano BISSEXTO!')
else:
    print(f'{ano} NÃO é ano BISSEXTO!')