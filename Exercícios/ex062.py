"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."""

from time import sleep

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
cont = 1
pa = primeiro_termo
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(pa, end=', ')
        pa += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Ao todo foram mostrados {} termos.'.format(total))
print('Finalizando...')
sleep(2)
print('{:=^40}'.format(' FIM '))
