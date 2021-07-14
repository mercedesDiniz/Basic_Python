# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Insira um ANO para Avaliação ou Zero para o ano atual: '))
if ano == 0:
    ano = date.today().year  # Vai pega só o ano da data atual
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0 :
    print('O Ano {} \033[32mÉ BISSEXTO\033[m!'.format(ano))
else:
    print('O Ano {} \033[31mNÃO É BISSEXTO\033[m!'.format(ano))