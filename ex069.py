times = ('Atletico', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',
         'Athletico', 'Cuiabá', 'São Paulo', 'Internacional')
print('-='*20)
print(f'Times do Brasileirão: {times} ')
print(f'Os cinco primeiros são {times[:5]}')
print(f'Os quatro últimos são {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
print(f'O time do Flamengo está na {times.index("Flamengo")+1} posição')