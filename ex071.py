val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
val3 = int(input('Digite mais um valor: '))
val4 = int(input('Digite novamente um valor: '))
numeros = (val1, val2, val3, val4)
print(f'Você digitou os valores {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3)+1}º posição')
pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
print(f'Foram digitados {pares} pares')
