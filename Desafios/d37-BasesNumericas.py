''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

print()
print('='*20, 'Conversor de Bases Numéricas', '='*20)
print()

num = int(input('Digite um número: '))

print('Escolha a base númerica que deseja converter:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL ')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido em BINÁRIO é: {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido em OCTAL é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido em HEXADECIMAL é: {hex(num)[2:]} ')
else:
    print('OPÇÃO INVALIDA!')
