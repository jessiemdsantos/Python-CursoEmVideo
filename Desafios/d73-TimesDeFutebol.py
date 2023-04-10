'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética.
d) Em que posição está o time da Botafogo. '''

tabela = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional',
          'Athletico-PR', 'Atlético-MG', 'Santos', 'América-MG', 'Red Bull Bragantino',
          'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará',
          'Cuiabá-MT', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('=' * 80)
print('{:^80}'.format('BRASILEIRÃO 2022'))
print('=' * 80)
print(f'Lista de times:\n{tabela}')
print('-' * 80)
print(f'Os 5 primeiros colocados:\n{tabela[:5]}')
print('-' * 80)
print(f'Os 4 últimos colocados:\n{tabela[-4:]}')
print('-' * 80)
print(f'Todos os times, em ordem alfabética:\n{sorted(tabela)}')
print('-' * 80)
print(f'O Botafogo está na {tabela.index("Botafogo")+1}ª posição.')
