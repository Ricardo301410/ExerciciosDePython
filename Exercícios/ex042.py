"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

r1 = float(input('Informe o tamanho da primeira reta: '))
r2 = float(input('Informe o tamanho da segundaa reta: '))
r3 = float(input('Informe o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r3 + r2 and r3 < r1 + r2:
    print('As medidas acima formam um triângulo ', end='')
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('EQUILÁTERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('ISÓCELES.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO.')
else:
    print('As medidas acima não formam um triangulo.')
