"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

nome = ' '
alunos = []
notas = []
medias = []
notasTemp = []
nota1 = nota2 = media = mostraNota = 0
while True:
    alunos.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notasTemp.append(nota1)
    notasTemp.append(nota2)
    notas.append(notasTemp[:])
    notasTemp.clear()
    continua = ' '
    while continua not in 'NS':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
for c in range(0, len(notas)):
    for v in range(0, 2):
        media += notas[c][v]
    media = media / 2
    medias.append(media)
    media = 0
print(f'='*40)
print(f'{"Nº":>2} --- {"NOME"} --- {"MEDIA":>4}')
print(f'-'*22)
for c in range(0, len(alunos)):
    print(f'{c} {alunos[c]:>11} {medias[c]:>7}')
print('-'*30)
while True:
    mostraNota = int(input('Mostrar nota de qual aluno?(Escolher por Nº) (999 interrompe): '))
    if mostraNota == 999:
        break
    else:
        print(f'Notas de {alunos[mostraNota]} são {notas[mostraNota]}')
print('Finalizando...')
print(f'Volte sempre!')
