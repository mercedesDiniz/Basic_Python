# Curso em Video - Curso de Python 3 - aula17
# Variáveis Compostas: LISTAS 
# Link: https://www.youtube.com/watch?v=N1hTsbW50eM&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=8

'''Listas são coleções heterogêneas de objetos, que podem ser de qualquer tipo, inclusive outras listas. As listas no Python são MUTÁVEIS. podendo ser alteradas a qualquer momento. Podem ser fatiadas da mesma forma que as strings '''

# Criando LISTAS:
lista01 = ['Termo01', 'Termo02', 'Termo03', 'Termo04'] 
print(f'\nLista 01 Original: {lista01}')
print(f'Tamanho: {len(lista01)}') # retorna o tamanho/ quantidade de elementos

# Adicionando Elementos: 
lista01.append('Termo05') # nome_lista.append(elemento) (vai para o final da lista)
print(f'Lista 01 apos Adição simples: {lista01}')

lista01.insert(0,'Termo0') # nome_lista.insert(posição,elemento) (pode determinar a posição)
print(f'Lista 01 após Insert: {lista01}')

# Removendo Elementos:
del lista01[5] # ref. pelo indice
lista01.pop(4) # ref. pelo indice
lista01.pop()  # remove o ultimo 
if 'Termo0' in lista01: # p/ garantir q o elemento exista na lista
    lista01.remove('Termo0') # ref. pelo valor (o primeiro que aparece)

print(f'Lista 01 após Remoções: {lista01}') 

# Converter outras sequências em Lista:
tupla = (6, 5, 3, 9, 2, 1, 4, 7, 8)
lista02 = list(range(4,11)) # transformar essa sequência em uma lista
lista03 = list(tupla) # transforma tuplas em listas

print(f'\nLista 02 Original: {lista02}')
print(f'Tamanho: {len(lista02)}') # retorna o tamanho/ quantidade de elementos

print(f'\nLista 03 Original: {lista03}')
print(f'Tamanho: {len(lista02)}') # retorna o tamanho/ quantidade de elementos

# Ordenação:
# print(f'Lista 03 Ordem Crescente: {lista03.sort()}') # modifica a própria lista
print(f'Lista 03 Ordem Crescente: {sorted(lista03)}') 
# print(f'Lista 03 Ordem Decrescente: {lista03.sort(reverse=True)}')
print(f'Lista 03 Ordem Crescente: {sorted(lista03, reverse=True)}') 
