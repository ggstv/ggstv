from random import randint
import operator
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
print(f'{"VALORES SORTEADOS"}')
print(jogo)
ranking = {}
for k, v in jogo.items():
    print(k, v)
ranking = sorted(jogo.items(), key=operator.itemgetter(1))
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i} {v[0]} tirou {v[1]}')