"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

print('Os números pares no intervalo de 1 a 50 são:')
for numeros in range(2, 51, 2):
    print(numeros, end=', ')
