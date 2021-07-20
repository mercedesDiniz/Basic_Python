# Curso em Video - Curso de Python 3 - aula14
# Estrutura de Repetição WHILE (Emquanto)

#Obs.: util para quando não sabemos o limite

# enquanto condiçaotalforVerdade         while condiçaotalforVerdade:
#   bloco de instruçoes                     bloco de intruçoes   

# Ex. 01
'''i = 1
while  i <= 10 : 
    print(i)
    i += 1
print('FIM') '''

# Ex. 02
'''resp = 'S'
while resp == 'S':
    n = int(input('Insira um numero: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
print('FIM')'''    

# Ex. 03
n = 1
total_npar = total_nimpar = 0
while n != 0:
    n = int(input('Insira um Número: '))
    if n != 0:
        if n % 2 == 0:
            total_npar += 1
        else:
            total_nimpar += 1            
print('Classificação:\n {} numeros PARES\n {} numeros IMPARES'.format(total_npar, total_nimpar))    