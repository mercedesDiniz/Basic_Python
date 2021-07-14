# Curso em Video - Curso de Python 3 - aula09
# Manipulando Cadeia de Texto/ Caractere/ String

# -Divisão e Junção:
#   nomeDaVariavel.split()  ->  divisão considerando os espaços, gera um lista com todas as palavra de um cadeia de caracteres
#   '-'.join(nomeDaVariavel)  ->  junta todos os elementos com o '-' entre eles

print('{:=^60}'.format('    DIVISÃO '))

frase = 'Curso em Video Python'

print('A frase é : {}'.format(frase))
frase = frase.split()
print('frase.split() = {}.'.format(frase))
frase = '-'.join(frase)
print(''"'-'"'.join(frase) = {}.'.format(frase))