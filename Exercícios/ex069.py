"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

cont_18 = cont_h = cont_m = 0
while True:
    print('{:=^29}'.format(' CADASTRE UMA PESSOA '))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:' )).strip().upper()[0]
    print('-' * 29)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 29)
    if continuar == 'N':
        break
    if idade >= 18:
        cont_18 += 1
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20:
        cont_m += 1
print('~' * 35)
print('Ao todo temos:')
print(f'{cont_18} pessoas com mais de 18 anos')
print(f'{cont_h} homens cadastrados')
print(f'{cont_m} mulheres com menos de 20 anos.')
print('~' * 35)
