"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número: '))
cor = {'verde': '\033[32m', 'azul': '\033[34m', 'vermelho': '\033[31m', 'limpa': '\033[m'}
print('''Escolha a base de conversão:
{}[ 1 ] Binário{}
{}[ 2 ] Octal{}
{}[ 3 ] Hexadecimal{}'''.format(cor['verde'], cor['limpa'], cor['azul'], cor['limpa'], cor['vermelho'], cor['limpa']))
conv = int(input('Sua opção: '))
if conv == 1:
    print('{} convertido para Binário é igual a {}{}{}'.format(num, cor['verde'], bin(num)[2:], cor['limpa']))
elif conv == 2:
    print('{} convertido para Octal é igual a {}{}{}'.format(num, cor['azul'], oct(num)[2:], cor['limpa']))
elif conv == 3:
    print('{} convertido para Hexadecimal é igual a {}{}{}'.format(num, cor['vermelho'], hex(num)[2:], cor['limpa']))
else:
    print('Opção inválida. Tente novamente.')
