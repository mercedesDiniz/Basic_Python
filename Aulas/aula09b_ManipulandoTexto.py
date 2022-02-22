# Curso em Video - Curso de Python 3 - aula09
# Manipulando Cadeia de Texto/ Caractere/ String

# -Análise:
#   len(nomeDaVariavel)  - comprimento
#   nomeDaVariavel.count('caractereEspecifico') - contar quantos do caractere aparecem na variavel
#   nomeDaVariavel.count('caractereEsp,indInicio,indFinal') - contar aparti de um fatiamento
#   nomeDaVariavel.find('trechoEspecificado') - retorna a indice do inicio do trecho especificado, se não houve, retorna -1
#   'trechoEspecifico'in nomeDaVariavel - retorna True/False se o trecho estiver presente ou não

print('{:=^60}'.format(' ANÁLISE '))

frase = 'Curso em Video Python'

print('A frase é : {}'.format(frase))
print('len(frase) = {}'.format(len(frase)))
print('frase.count('"'o'"') = {}'.format(frase.count('o')))
print('frase.count('"'o'"',0,13) = {}'.format(frase.count('o',0,13)))
print('frase.find('"'deo'"') = {}'.format(frase.find('deo')))
print('frase.find('"'xxx'"') = {}'.format(frase.find('xxx')))
print(''"'Curso'in frase"' = {}'.format('Curso'in frase))