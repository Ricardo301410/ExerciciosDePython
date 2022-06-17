""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

cont = 0
numeros = (int(input('Digite o 1º numero: ')), int(input('Digite o 2º numero: ')), int(input('Digite o 3º numero: ')), int(input('Digite o 4º numero: ')))
print(f'Você digitou os números {numeros}')
print(f'Ao todo o número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
