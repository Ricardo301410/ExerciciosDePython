"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
valor_1 = int(input('Digite o 1º valor: '))
valor_2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma opção
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = valor_1 + valor_2
        print('A soma de {} + {} é {}'.format(valor_1, valor_2, soma))
    elif opcao == 2:
        multi = valor_1 * valor_2
        print('A multiplicação de {} x {} é {}'.format(valor_1, valor_2, multi))
    elif opcao == 3:
        if valor_1 > valor_2:
            maior = valor_1
        elif valor_1 < valor_2:
            maior = valor_2
        print('O maior valor entre {} e {} é {}'.format(valor_1, valor_2, maior))
    elif opcao == 4:
        print('Informe os números novamente!')
        valor_1 = int(input('Digite o 1º valor: '))
        valor_2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente.')
    print('-=' * 10)
    sleep(2)
print('{:-^40}'.format(' Fim do programa '))
