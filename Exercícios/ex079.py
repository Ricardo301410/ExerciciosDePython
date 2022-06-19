"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = list()

while True:
    valores.append(int(input('Digite um número: ')))
    for n in valores:
        if n in valores:
            valores.remove(n)
    '''continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break'''
    if n == 00:
        break
print(f'Os valores únicos digitados foram {valores}')
