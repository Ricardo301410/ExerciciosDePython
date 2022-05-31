# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Qual é o seu nome? ')
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'azul': '\033[34m'}
print('{}É um prazer te conhecer, {}{}{}!'.format(cores['verde'], cores['azul'], nome, cores['verde']))
