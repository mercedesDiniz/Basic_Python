# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com ela: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prozo.

from datetime import date
ano_nascimento = int(input('Insira seu ano de nascimento: '))
ano_atual = date.today().year  # Vai pega só o ano da data atual
idade = ano_atual - ano_nascimento

if idade == 18:
    print('Esta na hora de se Alistar no Serviço Militar!')
elif idade < 18:
    print('Voce ainda vai se Alistar no Serviço Militar.\nFalta(m) {} ano(s).'.format(18-idade)) 
elif idade > 18:
    print('Já passou do tempo do alistamento tem {} ano(s).'.format(idade-18)) 