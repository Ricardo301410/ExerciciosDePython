"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:' )).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    