"""Desenvolva um programa que pergunte a distância de uma viagem em Km e calcule o preço da passagem. Cobrando R$0,
50 por Km para viagem de até 200Km e R$0,45 para viagens mais longas."""

d = float(input('Qual a distancia da viagem? '))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('A sua passagem vai custar R${:.2f}'.format(preço))
