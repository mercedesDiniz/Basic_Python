# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice 

print('{:=^20}'.format('SORTEIO p/ APAGAR O QUADRO'))
a1 = input('Insira o nome do/a Aluno/a 01: ')
a2 = input('Insira o nome do/a Aluno/a 02: ')
a3 = input('Insira o nome do/a Aluno/a 03: ')
a4 = input('Insira o nome do/a Aluno/a 04: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista) # metodo que sorteia um item da lista
print('O/A aluno/a sorteado/a foi o/a {}!'.format(escolhido))