"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
n_esimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, n_esimo_termo + razao, razao):
    print(c, end=', ')
print('fim!')
