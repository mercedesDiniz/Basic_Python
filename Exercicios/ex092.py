# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acado o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salãrio. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição para o exercicio).

from datetime import datetime
ano_Atual = datetime.now().year

trabalhador = {
    'Nome': str(input('Nome: ')),
    'Idade': ano_Atual - int(input('Ano de Nascimento: ')),
    'CTPS': int(input('Carteira de Trabalho (0 não tem): ')),
}

if trabalhador['CTPS'] != 0 :
    trabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Ano de Contratação'] + 35) - ano_Atual)

print('-*-'*30)
for k, v in trabalhador.items():
    print(f'\t- {k}: {v}')