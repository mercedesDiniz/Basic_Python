# Crie um programa que leia nome e duas notas de vários alunos e guande tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

dados = []
alunos = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 01: ')))
    dados.append(float(input('Nota 02: ')))
    dados.append((dados[1]+dados[2])/2) # calculo da media
    alunos.append(dados[:])
    dados.clear() # p/ "lispar" os dados
    continuar = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    
print('-='*40,'\n',f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}','\n','-'*40)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {a[3]:^8}')
print('-'*40)

detalhes = int(input('Mostrar notas de qual aluno? (999 - Finaliza): '))
while detalhes != 999:
    print(f'Notas do(a) {alunos[detalhes][0]} são: {alunos[detalhes][1]} e {alunos[detalhes][2]}')
    detalhes = int(input('Mostrar notas de qual aluno? (999 - Finaliza): '))