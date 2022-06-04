"""Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pesar em um número entre 0 e 10. Tente adivinhar...')
acertou = False
con_palpite = 0
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    con_palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais alto!')
        if jogador > computador:
            print('Um pouco mais baixo!')
print('PARABÉNS, você acertou na {}ª tentativa.'.format(con_palpite))
