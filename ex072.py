produtos = ('Lápis', 3, 'Borracha', 1.75, 'Caderno', 15.90, 'Estojo', 7.90,
            'Régua', 4.50, 'Mochila', 45.90, 'Marca-Texto', 6.90)
print('='*50)
print(f'{"LISTAGEM DE PRECOS":^50}')
print('='*50)
for prod in range(0, len(produtos), 2):
    print(f'{produtos[prod]:.<40}', f'R$ {produtos[prod+1]:>6.2f}')
