print('='*50)
print(f'{"Contador DE Vogais":^50}')
print('='*50)

palavras = ('Tesoura', 'Calculadora', 'Caixa','Papel', 'Monitor', 'Caneca', 'Controle', 'Fone', 'Cotonete',
            'Escova', 'Raquete')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in range(len(palavras)):
    vogal = []
    for c in palavras[palavra]:
        if c in vogais:
            vogal.append(c)
    print(f'A palavra {palavras[palavra]:^12} contém as vogais {vogal}')

