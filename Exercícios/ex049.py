"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

numero = int(input('Digite um número para saber sua tabuada: '))
cores = {'azul': '\033[34m', 'verde': '\033[32m', 'roxo': '\033[35m', 'limpa': '\033[m'}
print('{}*'.format(cores['azul']) * 15)
print('{}Tabuada de {}{}'.format(cores['roxo'], cores['verde'], numero))
print('{}*{}'.format(cores['azul'], cores['limpa']) * 15)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(numero, c, numero * c))
