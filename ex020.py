# Um professor quer sortear a ordem de apresentação dos alnos. Faça um programa que leia o nome dos quadro alunos e mostre a ordem sorteada.

from random import shuffle

print('{:=^20}'.format('SORTEIO p/ APRESENTAÇÃO'))
a1 = input('Insira o nome do/a Aluno/a 01: ')
a2 = input('Insira o nome do/a Aluno/a 02: ')
a3 = input('Insira o nome do/a Aluno/a 03: ')
a4 = input('Insira o nome do/a Aluno/a 04: ')

lista = [a1, a2, a3, a4]
shuffle(lista) # metodo que "embaralha" a lista
print('A Ordem de apresentação segue com :\n {}'.format(lista))