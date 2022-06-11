""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

numero = int(input('Digite um número: '))
cont = 0
flag = 999
while numero != 999:
    numero = int(input('Digite mais um número: '))
    cont += 1
print('Foram informados {} numeros e a soma deles é {}.'.format(cont - flag))
