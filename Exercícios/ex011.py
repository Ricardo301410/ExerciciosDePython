"""Fassa um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m²."""

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da arede? '))
area = altura * largura
tinta = area / 2
print('A sua parede tem {}m² e você vai precisar de {}l de tinta para pintá-la.'.format(area, tinta))
