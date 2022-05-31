"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
from datetime import date
nasc = int(input('Informe o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos, portanto é da categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, portanto é da categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos, portanto é da categoria JÚNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos, portanto é da categoria SÊNIOR.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, portanto é da categoria MASTER.'.format(idade))
