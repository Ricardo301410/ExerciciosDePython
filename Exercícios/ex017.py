"""Faça um programa que leia o comprimento do cateto oposto a do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa."""

from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}.'.format(hi))
