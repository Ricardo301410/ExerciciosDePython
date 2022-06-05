"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Sexo [M/F]: ')).upper()
atual = date.today().year
idade = atual - nasc
if sexo == 'F':
    print('Você não precisa fazer alistamento!')
elif idade == 18:
    print('Você tem {} anos e deve se alistar IMEDIATAMENTE!'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você tem {} anos e ainda faltam {} para o seu alistamento que será em {}.'.format(idade, saldo, ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você tem {} anos e já passaram {} anos do seu alistamento que foi em {}.'.format(idade, saldo, ano))
