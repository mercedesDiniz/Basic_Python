# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year  # Vai pega só o ano da data atual

cont_menores = 0
cont_maiores = 0
j = 1

for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(j)))
    j += 1
    if ano_atual-ano_nascimento >= 21 :
        cont_maiores += 1
    else:
        cont_menores += 1    

print('Das pessoas cadrastradas, {} ja atingiram a maioridade, e {} ainda são menores.'.format(cont_maiores, cont_menores))