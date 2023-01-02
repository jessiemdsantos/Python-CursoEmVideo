''' Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO,
Média 7.0 ou superior: APROVADO'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
if n1 > 10 or n2 > 10:
    print('ATENÇÃO: As notas precisam estar entre 0 e 10! Tente novamente!')
else:
    media = (n1 + n2) / 2
    if media < 5:
        print(f'Média = {media} (abaixo de 5.0). Aluno \033[31mREPROVADO!\033[m')
    elif media < 7:
        print(f'Média = {media} (entre 5.0 e 6.9). Aluno em \033[33mRECUPERAÇÃO!\033[m')
    else:
        print(f'Média = {media} (entre 7.0 e 10). Aluno \033[32mAPROVADO!\033[m')


