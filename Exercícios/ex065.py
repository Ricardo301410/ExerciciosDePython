"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

cont = soma = 0
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    soma += numero
    cont += 1
media = soma / cont
print('A média dos números digitados foi {}.'.format(media))
