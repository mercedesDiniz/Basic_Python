# Faça um programa que leia o nome e média de UM aluno, guardando também a situação (Aprovado / Reprovado) em um dicionario. No final, moste o conteudo da estruturana tela.

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

print('-'*40,'\nDADOS DO ALUNO:')
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'\t- {k}: {v}')