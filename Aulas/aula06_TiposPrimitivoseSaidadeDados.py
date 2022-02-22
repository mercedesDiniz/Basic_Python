# Curso em Video - Curso de Python 3 - aula06
# Tipos Primitivos :
# int - numeros inteiros
# float - numeros reais
# bool - valores logicos - True ou False
# str - caracteres ou strings - entre aspas simples ou não

# Ex.01
# print('=== PROGRAMA SOMA SIMPLES ===')
# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite um numero: '))
# s = n1+n2
# print('O valor da soma de {} + {} = {}'.format(n1, n2, s))

# Ex.02 - type()
print(' === AVALIAÇÃO DO TIPO PRIMITIVO ===')
string1 = input('Digite uma string : ')
print(type(string1))
numInteiro = int(input('Digite um numero inteiro: '))
print(type(numInteiro))
numReal = float(input('Digite um numero real: '))
print(type(numReal))
valorLogico = bool(input('Digite um valor logico: '))
print(type(valorLogico))
print(valorLogico)  # se tiver um valor dentro na variavel ela é verdadeiro, se não ela é falsa