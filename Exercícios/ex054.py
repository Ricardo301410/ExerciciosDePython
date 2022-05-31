"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores."""

from datetime import date
menor = 0
maior = 0
ano_atual = date.today().year
for c in range(1, 8):
    nascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = ano_atual - nascimento
    if idade < 18:
        menor += 1
    if idade >= 18:
        maior += 1
print('Dos anos de nascimento digitados acima, tem {} pessoas menores e {} maiores de idade.'.format(menor, maior))
