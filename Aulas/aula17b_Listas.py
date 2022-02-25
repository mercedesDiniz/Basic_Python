# Curso em Video - Curso de Python 3 - aula17
# Variáveis Compostas: LISTAS 

# Ex.01:
lista01 = list() # lista vazia
print(len(lista01))
for i in range(0, 5): 
    lista01.append(int(input('Insira um valor: ')))

for posicao, valor in enumerate(lista01):
    print(f'Posição: {posicao} - Elementos: {valor}')
print(f'Fim da lista! Ela tem {len(lista01)} elementos.')

# Ex.02: LIGAÇÃO ENTRE LISTAS
listaA = [2, 4, 6, 8]
listaB = listaA  # Uma LIGAÇÃO é estabelecida
print(f'\nLista Original: A: {listaA} e B: {listaB}.')

listaB[2] = 10 # Alteração afeta as duas listas.
print(f'Lista A: {listaA}.')
print(f'Lista B: {listaB}.')

# Ex.03: COPIA DE LISTAS
listaA = [2, 4, 6, 8]
listaB = listaA[:]  # RECEBENDO todos os elementos (uma copia) 
print(f'\nLista Original: A: {listaA} e B: {listaB}.')

listaB[2] = 10 
print(f'Lista A: {listaA}.')
print(f'Lista B: {listaB}.')