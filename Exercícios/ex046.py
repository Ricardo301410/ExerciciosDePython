"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""

from emoji import emojize
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':fogos_de_artifício:', language='pt'))
