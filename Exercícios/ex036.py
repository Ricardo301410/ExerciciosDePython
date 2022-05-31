"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado."""

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Em quantos anos de financiamento? '))
parcela = casa / (anos * 12)
maxima = salario * (30 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos a parcela será de R${:.2f} cada.'.format(casa, anos, parcela))
if parcela <= maxima:
    print('\033[32mEmpréstimo APROVADO!')
else:
    print('\033[31mEmpréstimo NEGADO!')
