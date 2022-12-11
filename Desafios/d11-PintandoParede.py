'''Faça um programa que leia a largura e a altura de uma parede, em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la sabendo que, cada litro de tinta,
pinta uma área de 2m². '''

a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))

area = a * l
res = area / 2
print()
print(f'Área total: {area}m²')
print(f'Serão necessários {res:.1f} litros de tinta para pintar essa parede.')