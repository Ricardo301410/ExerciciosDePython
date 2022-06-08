"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""

numero = int(input('Digite quantos termos você quer mostrar: '))
termo_1 = 0
termo_2 = 1
print('{}, {}'.format(termo_1, termo_2), end=', ')
cont = 3
while cont <= numero:
    termo_3 = termo_1 + termo_2 # 1
    print('{}'.format(termo_3), end=', ')
    termo_1 = termo_2 # 1
    termo_2 = termo_3 # 2
    cont += 1 # 4
print('fim')
