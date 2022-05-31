"""Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada km acima do limite."""

v = float(input('Qual a sua velocidade? '))
multa = (v - 80) * 7
if v <= 80:
    print('Parabéns! você está dentro do limite de velocidade.')
else:
    print('Você foi multado em R${:.2f} por exceder o limite de velocidade de {:.0f}Km/h.'.format(multa, 80))
