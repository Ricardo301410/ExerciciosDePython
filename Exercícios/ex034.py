"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual o valor do seu salário? R$'))
au1 = salario + (salario * 15 / 100)
au2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print('Parabéns! você ganhou um aumento de 15% e o seu novo salário será de R${:.2f}.'.format(au1))
else:
    print('Parabéns! você ganhou um aumento de 10% e o seu novo salário será de R${:.2f}.'.format(au2))
