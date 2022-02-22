# Crei um programa que leia uma frase qualquer e diga se ela é um PALÌNDROMO, desconsiderando os espaços e acentos.
# Ex. de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Insira a Frase: ')).strip().upper() # tiramdo os espaços do inicio e fim, e colocando tuno p/ maiusculo

# Eliminando os espaços internos:
palavras = frase.split()  # fatiando pelos espaços entre as palavras e colocando em um lista
junto = ''.join(palavras) # juntando os elementos da lista sem espaços

frase_invertida = ''

# Invertendo a frase tratada:
frase_invertida = junto[::-1] # Metodo com Fatiamento
'''# Metodo com laço FOR:
for letra in range(len(junto)-1, -1, -1 ):
    frase_invertida += junto[letra]'''

print('A frase fica \033[33m{}\033[m e invertiva fica \033[33m{}\033[m.'.format(junto, frase_invertida))

# Verificando a condição de Palíndromo:
if frase_invertida == junto :
    print('\033[32mA frase é um Palíndromo!\033[m')
else:
    print('\033[31mA frase não é um Palíndromo!\033[m')    