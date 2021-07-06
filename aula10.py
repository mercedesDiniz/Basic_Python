# Curso em Video - Curso de Python 3 - aula10
# Condições - Parte 1

# if objeto.nomeDoMetodo():
#   bloco de instruções True  
# else:  
#   bloco de instruções False


# 1 modelo: Condição Composta
tempo = int(input('Quantos anos o seu carro tem? '))
if tempo <=3:
    print('Carro Novo!')
else:   
    print('Carro Velho!')
print('--FIM--')

# 2 modelo: Codição Simplificada
# tempo = int(input('Quantos anos o seu carro tem? '))
# print('Carro Novo!'if tempo<=3 else'Carro Velho!')
# print('--FIM--')



# Ex.01
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Mercedes':
    # print('Belo nome.')
# else:
    # print('Que nome sem sal.')    
# print('Bom dia, {}!'.format(nome))

# Ex.02
# n1 = float(input('Insira a Primeira Nota: '))
# n2 = float(input('Insira a Segunda Nota: '))
# m = (n1+n2)/2
# print('Sua Media foi {:.2}.'.format(m))
# if m >= 6.0:
    # print('Media Regular!')
# else:
    # print('Media Insuficiente!')    
