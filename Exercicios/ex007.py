# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('{:=^40}'.format('CALCULO NA MEDIA'))
nota1 = float(input('Insira a nota da primeira avaliação: '))
nota2 = float(input('Insira a nota da segunda avaliação: '))
media = (nota1+nota2)/2
print('Media = {:.3f}'.format(media))