"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

nome_maisvelho = 0
mais_velho = 0
cont_idade = 0
for pessoas in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    cont_idade += idade
'''if sexo == 'M' and idade > mais_velho:
    mais_velho = idade
    print('O nome do homem mais velho é {}'.format(nome))'''
media = cont_idade / 4
print('A média de idade do grupo é {}'.format(media))
