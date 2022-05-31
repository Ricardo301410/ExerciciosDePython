"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""


cont_idade = 0
mais_velho = 0
nome_maisvelho = ''
for pessoas in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    cont_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_maisvelho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_maisvelho = nome
media = cont_idade / 4
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(mais_velho, nome_maisvelho))
