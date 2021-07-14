# Curso em Video - Curso de Python 3 - aula12
# Condições Alinhadas

#  if condiçaoQualquer01:
#    bloco de instruções  
# elif condiçaoQualquer02:
#   bloco de instruções
#  else:  
#    bloco de instruções 

# Exemplo:
nome = str(input('Qual é o seu nome? '))
if nome == 'Mercedes' or nome == 'mercedes':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Esse nome é bem comum do Brasil!')   
elif nome in 'Ana Cláudia Jessica Julia':    
    print('jura? que legal !')     
else:
    print('Que nome sem-sal!')    
print('Tenha um Bom Dia, {}!'.format(nome))

#   'trechoEspecifico'in nomeDaVariavel - retorna True/False se o trecho estiver presente ou não