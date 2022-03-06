# Curso em Video - Curso de Python 3 - aula19
# Variáveis Compostas: DICIONÁRIOS
# Link: https://www.youtube.com/watch?v=ZWj8o692qGY&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=22&ab_channel=CursoemV%C3%ADdeo

'''Um dicionário é uma lista de associações compostas por uma chave única e estruturas correspondentes.
- São mutáveis
- Podemos ter indices literais '''

# Criando DICIONÁRIOS:    
# Dicionário Vazio: dicionario0 = dict() ou {} 
# dicionario = {'Identificador': valor}
dicionario_dados = {'nome':'Pedro', 'idade':25}
print(f'\n>>> Dicionário Original: {dicionario_dados}')

# Seleção de Elementos:
print(f'dicionario_dados[nome] = ', dicionario_dados['nome'])
print(f'dicionario_dados[idade] = ', dicionario_dados['idade'])

# Adicionando Elementos:
dicionario_dados['sexo'] = 'M' # já que o indice passado não existe, ele é criado 
print(f'>> Dicionário após adição do sexo: {dicionario_dados}')

# Remover elementos:
del dicionario_dados['idade'] # ref. pelo indice
print(f'>> Dicionário após remoção da idade: {dicionario_dados}')

# Ex.01:
filme01 = {
    'titulo':'Star Wars',
    'ano': 1977,
    'diretor':'George Lucas'
}
print(f'\n>>> Dicionário Filme: {filme01}')
print(f'>> VALORES: {filme01.values()}')
print(f'>> CHAVES: {filme01.keys()}')
print(f'>> ITENS: {filme01.items()}\n')

for k, v in filme01.items():
    print(f'O {k} é {v}') # print formatado

# Ex.02: Uma lista com um dicionário dentro.
locadora = list()
locadora.append(filme01)

locadora.append({
    'titulo':'Avagers',
    'ano': 2012,
    'diretor':'Joss Whedon'})

locadora.append({
    'titulo':'Matrix',
    'ano': 1999,
    'diretor':'Wachowski'})

print(f'\n>>> Lista LOCADORA com o DICIONARIO filme:')
for i in range(0, len(locadora)):
    print(f'Filme {i}: {locadora[i]}')

# Seleção de Elementos: lista[ref.Externa_Lista][ref.Interna_Dicionario]
print(f'locadora[0][ano] = ', locadora[0]['ano'])
print(f'locadora[2][titulo] = ', locadora[2]['titulo'],'\n')

# Ex.03: 
estado = dict()
brasil = list()

for i in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # metodo copy() copia o conteudo de um dicionario

print(f'>>> Lista BRASIL com o DICIONARIO ESTADO:')
for est in brasil: # p/ a lista
    for k, v in est.items(): # p/ o dicionário 
        print(f'\t{k} = {v}')
