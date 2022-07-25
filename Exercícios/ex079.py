"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = list()

while True:
    numero = (int(input('Digite um número: ')))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não adicionado...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Os valores únicos digitados foram {valores.sort()}')
