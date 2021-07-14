# Curso em Video - Curso de Python 3 - aula09
# Manipulando Cadeia de Texto/ Caractere/ String

# -Transformação:
#   nomeDaVariavel.replace('trechoAntigo','trechoNovo')  -> substituição
#   nomeDaVariavel.upper()  -> (p/ cima) formata tudo p/ maiusculas
#   nomeDaVariavel.lower()  -> (p/ baixo) formata tudo p/ minusculas
#   nomeDaVariavel.capitalize() -> deixa apenas o primeiro elemento em maiusculo, e formata o resto p/ minusculo 
#   nomeDaVariavel.title()  ->  formata p/ maiusculo o primeiro caractere e cada palavra
#   nomeDaVariavel.strip()  ->  remove todos os espação inuteis no inicio e final
#   nomeDaVariavel.rstrip()  ->  remove os espação inuteis no final (à direita)
#   nomeDaVariavel.lstrip()  ->  remove os espação inuteis no inicio (à esquerda)

print('{:=^60}'.format(' TRANSFORMAÇÃO '))

frase = 'Curso em Video Python'

print('A frase é : {}'.format(frase))
print('frase.replace('"'Python'"','"'Androide'"') = {}'.format(frase.replace('Python','Androide')))
print('frase.upper() = {}'.format(frase.upper()))
print('frase.lower() = {}'.format(frase.lower()))
print('frase.capitalize() = {}'.format(frase.capitalize()))
print('frase.title() = {}'.format(frase.title()))

frase1 = '   Aprenda Python  '
print('A frase1 é : {}.'.format(frase1))
print('frase1.strip() = {}.'.format(frase1.strip()))
print('frase1.rstrip() = {}.'.format(frase1.rstrip()))
print('frase1.lstrip() = {}.'.format(frase1.lstrip()))