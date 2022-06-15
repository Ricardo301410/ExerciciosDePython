"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('{:=^40}'.format(' BANCO STARK '))
print('-' * 40)
print('Cédulas disponíveis: 50, 20, 10 e 1')
print('-' * 40)
valor_saque = int(input('Valor do saque: R$ '))
total = valor_saque
cedula = 50
cont_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        cont_cedula += 1
    else:
        if cont_cedula > 0:
            print(f'Total de {cont_cedula} cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont_cedula = 0
        if total == 0:
            break
print('-' * 40)
print('Volte sempre ao Banco Stark! Tenha um bom dia!')
