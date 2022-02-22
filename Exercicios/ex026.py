# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('Aparece pela primeira vez na posição de indice {}.'.format(frase.find('A')+1)) # retorna a indice do inicio do trecho especificado, se não houve, retorna -1
print('Aparece pela última vez na posição de indice {}.'.format(frase.rfind('A')+1))  # o rfind procura aparti do lado direito  