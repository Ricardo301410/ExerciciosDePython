"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

cont = total = prod1000 = menor = 0
nomemenor = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do pruto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        prod1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        nomemenor = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R$ {total:.2f}')
print(f'{prod1000} produtos custaram mais de R$ 1000,00')
print(f'O pruto mais barato foi {nomemenor} que custou R$ {menor:.2f}')
