# Crie uma programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(anoN):
    idade = datetime.now().year - anoN
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'

ano_Nasc = int(input('Em que anos você nasceu? '))
voto(ano_Nasc)
