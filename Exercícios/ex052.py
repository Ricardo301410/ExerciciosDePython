"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

cont = 0
numero = int(input('Informe um número para saber se é primo: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO numero {} foi divisível {} vezes,'.format(numero, cont), end=' ')
if cont == 2:
    print('por isso ele é PRIMO!')
else:
    print('por isso ele NÃO É PRIMO!')
