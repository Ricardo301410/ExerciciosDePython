"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

numero = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
cont = numero
while cont > 0:
    fatorial *= cont
    cont -= 1
print('O resultado de {}! = {}'.format(numero, fatorial))
