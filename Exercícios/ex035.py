"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
 triângulo."""

from time import sleep
r1 = float(input('Informe o tamanho da primeira reta: '))
r2 = float(input('Informe o tamanho da segunda reta: '))
r3 = float(input('Informe o tamanho da terceira reta: '))
print('{}Analizando as medidas...{}'.format('\033[1;34m', '\033[m'))
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas acima {}formam{} um triângulo.'.format('\033[1;31m', '\033[m'))
else:
    print('As medidas acima {}não formam{} um triangulo.'.format('\033[1;31m', '\033[m'))
