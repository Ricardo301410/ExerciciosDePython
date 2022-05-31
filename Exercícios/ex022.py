"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas;
O nome com todas as letras minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome."""

from time import sleep
nome = str(input('Digite seu nome completo: '))
print('Analizando seu nome...')
sleep(2)
print('Seu nome em maiusculo: {}.'.format(nome.upper()))
print('Seu nome em minúsculo: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome.strip()) - nome.count(' ')))
dividido = nome.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(dividido[0], len(dividido[0])))
