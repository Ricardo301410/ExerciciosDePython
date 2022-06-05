"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
pa = primeiro_termo
print('Os 10 primeiros termos da PA são:', end=' ')
while cont <= 10:
    print(pa, end=', ')
    pa += razao
    cont += 1
print('fim!')
