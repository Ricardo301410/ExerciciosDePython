# Fassa um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o seu salário? R$ '))
aumento = salario + (salario * 15 / 100)
print('O seu salário que era R$ {:.2f}, com 15% de aumento ficará R$ {:.2f}.'.format(salario, aumento))
