# Fassa um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Insira o preço do produto: R$ '))
desc = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f}, ficará R$ {:.2f} com 5% de desconto.'.format(preco, desc))
