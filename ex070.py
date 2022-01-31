import random

numeros = tuple(random.randint(1, 10) for c in range(5))
print(numeros)

maior = max(numeros)
menor = min(numeros)

print(f'O maior é {maior} e o menor é o {menor}')