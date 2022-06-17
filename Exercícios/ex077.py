"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for pal in palavras:
    print(f'\nNa palavra {pal.upper()} temos: ', end='')
    for letra in pal:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
