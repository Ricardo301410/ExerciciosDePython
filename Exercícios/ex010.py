# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem? R$ '))
dolar = real / 4.70
print('Com R${:.2f} você poderá comprar US${:.2f}.'.format(real, dolar))
