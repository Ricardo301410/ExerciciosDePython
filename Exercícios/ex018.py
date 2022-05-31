# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulodesejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {}, tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente de {:.2f}.'.format(angulo, seno, cosseno,
                                                                                                 tangente))
