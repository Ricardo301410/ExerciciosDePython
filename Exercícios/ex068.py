"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

cont = 0
print('Vamos jogar par ou ímpar?')
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} e total foi {total}', end=', ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-' * 40)
print(f'GAME OVER! Você venceu {cont} vezes.')
