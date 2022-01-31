numeros = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continua = ' '
while True:
    num = int(input('Digite um numero de 0 a 20: '))
    while num >= 20 or num < 0:
        print(f'Fora do alcance, digite novamente.', end=' ')
        num = int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if continua in 'Nn':
        break
print('Acabou!')

