# Curso em Video - Curso de Python 3 - aula09
# Manipulando Cadeia de Texto/ Caractere/ String

# -Fatiamento:  
#   nomeDaVariavel[indiceDoCaracter]
#   nomeDaVariavel[indInicial:indFinal+1]
#   nomeDaVariavel[indInicial:indFinal+1:Saltos]
#   nomeDaVariavel[:indFinal+1]  (inicio no primeiro elemento(0))
#   nomeDaVariavel[indInicial:]  (final no ultimo elemento) 
#   nomeDaVariavel[indInicial::Saltos]  (final no ultimo elemento)


print('{:=^60}'.format(' FATIAMENTO '))

frase = 'Curso em Video Python'

print('A frase é : {}'.format(frase))
print('frase[15] = {}'.format(frase[15]))
print('frase[9:14] = {}'.format(frase[9:14]))
print('frase[9:21:2] = {}'.format(frase[9:21:2]))
print('frase[9::3] = {}'.format(frase[9::3]))
print('frase[:5] = {}'.format(frase[:5]))
print('frase[9:] = {}'.format(frase[9:]))