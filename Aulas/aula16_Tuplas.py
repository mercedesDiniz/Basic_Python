# Curso em Video - Curso de Python 3 - aula16 
# Variáveis Compostas: TUPLAS 
# Link: https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=1

'''As Variaveis Compostas são formadas por uma ou mais posições (campos ou entradas), podendo armazenar um ou mais dados (“estrutura” de armazenamento). Classificadas em homogêneas (vetoriais) ou heterogêneas (registros). Entre as existentes temos as : Tuplas, Listas e Dicionarios.
Obs.: As Tuplas são IMUTÁVEIS.'''

# Criando TUPLAS:
tupla01 = ('Termo01', 'Termo02', 'Termo03', 'Termo04') # parênteses são opcionais
print(f'Tupla: {tupla01}')

# Selecionando um Termo: nomeTupla[nTermo]:
print(f'tupla01[0] = {tupla01[0]}') 
print(f'tupla01[-1] = {tupla01[-1]}')

# Fatiamento:
print(f'tupla01[1:3] = {tupla01[1:3]}') 
print(f'tupla01[:2] = {tupla01[:2]}')
print(f'tupla01[-2:] = {tupla01[-2:]}')

print(f'len(tupla01) = {len(tupla01)}') # retorna o Comprimento/tamanho 

# Ex.01:
lanche = ('Pizza', 'Suco', 'Pudim', 'Miojo')
'''for comida in lanche:
    print(f'Vou comer {comida}!')'''
# Ex.02:
for posicao, comida in enumerate(lanche):
    print(f'Vou comer {comida}, na posição {posicao}.')
    
# Ex.03:
'''for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}, na posição {cont}.')'''

print(f'sorted(lanche) = {sorted(lanche)}')  # Colocando na Ordem 

# Ex.04:
tupla02 = (2, 5, 4)
tupla03 = (5,8,1,2)
tuplaConcatenacao = tupla02 + tupla03 # Contatenação de tuplas
print(tuplaConcatenacao)
print(tuplaConcatenacao.count(5)) # contar quantidade do termo especificado estão presentes 
print(tuplaConcatenacao.index(8)) # retorna a posição da primeiro ocorrencia do termo especificados

# Ex.05: Podemo ter dados de tipos diferentes dentro de uma mesma tuplas
pessoa = ('Mercedes', 22, 'F',55)
print(pessoa)

del(pessoa) # Apaga um TUPLA