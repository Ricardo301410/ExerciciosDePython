"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 40)
print(f'Os 20 colocados do Brasileirão são: {times}')
print('-=' * 40)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=' * 40)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-=' * 40)
print(f'Todos o colocados em ordem alfabética são: {sorted(times)}')
print('-=' * 40)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
print('-=' * 40)
