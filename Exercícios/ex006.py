# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
d = num * 2
t = num * 3
r = num ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(num, d, t, r))
