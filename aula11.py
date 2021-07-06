# Curso em Video - Curso de Python 3 - aula11
# Cores no Terminal

# Padrão ANSI - Ascape Sequence - \033[codEstilo;codCorTexto;codCorFundom

#   STYLE                                      TEXT      BACK 
#   0  Nenhum/None                  Branco      30        40
#   1  Negrito/Bold                 Vermelho    31        41
#   4  Sublinhado/Underline         Verde       32        42
#   7  Invete as Cores/Negative     Amarelo     33        43
#                                   Azul        34        44
#                                   Magenta     35        45
#                                   Ciano       36        46
#                                   Cinza       37        47

print('\033[0;30;41mMetodo 01, Teste de Cores 01\033[m')
print('\033[4;33;44mMetodo 01, Teste de Cores 02\033[m')
print('\033[1;35;43mMetodo 01, Teste de Cores 03\033[m')
print('\033[30;42mMetodo 01, Teste de Cores 04\033[m')
print('\033[mMetodo 01, Teste de Cores 05\033[m')
print('\033[7;30mMetodo 01, Teste de Cores 06\033[m')


variavel01 = 'Teste de Cores 07'
variavel02 = 'Teste de Cores 08'
variavel03 = 'Teste de Cores 09'
print('Metodo 02, {}{}{} !!!'.format('\033[4;34m', variavel01, '\033[m'))
print('Metodo 02, {}{}{} !!!'.format('\033[1;37;41m', variavel02, '\033[m'))
print('Metodo 02, {}{}{} !!!'.format('\033[1;31;40m', variavel03, '\033[m'))


cores = {'limpa':'\033[m', 
        'azul':'\033[34m',
        'amarelo':'\033', 
        'pretoEbranco':'\033[7;30m'} 
variavel04 = 'Teste de Cores 10'
variavel05 = 'Teste de Cores 11'
variavel06 = 'Teste de Cores 12'
print('Metodo 03, {}{}{} !!!'.format(cores['amarelo'], variavel04,cores['limpa']))
print('Metodo 03, {}{}{} !!!'.format(cores['azul'], variavel05,cores['limpa']))
print('Metodo 03, {}{}{} !!!'.format(cores['pretoEbranco'], variavel06,cores['limpa']))