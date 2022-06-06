"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""

numero = int(input('Digite um número: '))
ultimo = 1
penultimo = 1
if numero == 1 or numero == 2:
    print('1')
else:
    count = 3
    while count <= numero:
        termo = ultimo + penultimo # 2
        penultimo = ultimo # 1
        ultimo = termo # 2
        count += 1 # 4
print(termo)
