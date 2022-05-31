# fassa um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número para saber sua tabuada: '))
cores = {'azul': '\033[34m', 'verde': '\033[32m', 'roxo': '\033[35m', 'limpa': '\033[m'}
print('{}*'.format(cores['azul']) * 15)
print('{}Tabuada de {}{}'.format(cores['roxo'], cores['verde'], numero))
print('{}*{}'.format(cores['azul'], cores['limpa']) * 15)
print('{} X {:2} = {}'.format(numero, 1, numero * 1))
print('{} X {:2} = {}'.format(numero, 2, numero * 2))
print('{} X {:2} = {}'.format(numero, 3, numero * 3))
print('{} X {:2} = {}'.format(numero, 4, numero * 4))
print('{} X {:2} = {}'.format(numero, 5, numero * 5))
print('{} X {:2} = {}'.format(numero, 6, numero * 6))
print('{} X {:2} = {}'.format(numero, 7, numero * 7))
print('{} X {:2} = {}'.format(numero, 8, numero * 8))
print('{} X {:2} = {}'.format(numero, 9, numero * 9))
print('{} X {:2} = {}'.format(numero, 10, numero * 10))
