# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre: 1. A média de idade do grupo. 2. Qual é o nome do homem mais velho. 3. Quantas mulheres têm menos de 20 anos.

media_idade = 0 
idade_tota = 0
cont_homens = 0
idade_homemVelho = 0
nome_homemVelho = '***'
cont_mulheres20 = 0

for i in range(1, 5):
    print('-'*20, ' {} PESSOA '.format(i), '-'*20)
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()

    idade_tota += idade

    if sexo == 'MASCULINO' or sexo == 'M':
        cont_homens += 1
        if cont_homens == 1:
            idade_homemVelho = idade
            nome_homemVelho = nome
        if cont_homens != 0 and cont_homens != 1:
            if idade > idade_homemVelho:
                idade_homemVelho = idade
                nome_homemVelho = nome

    if sexo == 'FEMININO' or sexo == 'F' and idade < 20 :
        cont_mulheres20 += 1

media_idade = idade_tota/4
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=- ANALISE -=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('A média de idade do grupo é {}.'.format(media_idade))
print('O homem mais velho é o {}, e ele tem {} anos.'.format(nome_homemVelho, idade_homemVelho))
print('Este grupo tem {} mulher(es) com menos de 20 anos.'.format(cont_mulheres20))