"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
print('-'*30)
if aluno ['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')
