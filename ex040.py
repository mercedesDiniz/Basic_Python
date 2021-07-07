# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com ela: - Media abaixo de 5 é REPROVADO; entre 5 e 6,9 é RECUPERAÇÃO, e 7 ou mais é APROVADO.

print('\033[1;34m-=-\033[m'*30)
print('\033[1;36mAVALIANDO A MEDIA\033[m')
n1 = float(input('Insira a Primeira Nota: '))
n2 = float(input('Insira a Segunda Nota: '))

media = (n1+n2)/2

if media >= 7 :
    print('\033[32mAPROVADO!\033[m')
elif media >=5 and media <=6.9 :
    print('\033[33mRECUPERAÇÃO!\033[m')
elif media < 5 :
    print('\033[31mREPROVADO!\033[m')
print('\033[1;34m-=-\033[m'*30)  