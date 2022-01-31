def area(a, b):
    calc = a * b
    print(f'{calc}m²')


def title():
    print(f'-' * 60)
    print(f'{"":20}{"Controle de terrenos"}')
    print(f'-' * 60)


title()
larg = float(input('LARGURA: '))
comp = float(input('COMPRIMENTO: '))
area(larg, comp)
