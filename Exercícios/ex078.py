"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

maior = menor = 0
valores = list()
for p in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {p}: ')))
    if p == 0:
        maior =  menor = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        if valores[p] < menor:
            menor = valores[p]
print('-' * 50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
print(f'\n{" Fim ":-^50}')
