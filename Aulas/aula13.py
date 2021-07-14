# Curso em Video - Curso de Python 3 - aula13
# Estrutura de Repetição FOR

# laço i no intervalo (n1,n2)  ->   for i in range(n1,n2):
#    bloco de instruções                bloco de instruções

# Ex.01
for i in range(1,7):
    print('Teste Crescente {}'.format(i))
print('FIM ~ ex.01\n\n')

# Ex.02
for i in range(6,0,-1):
    print('Teste Decrescente {}'.format(i))
print('FIM ~ ex.02\n\n')

# Ex.03
for i in range(0,7,2):
    print('Teste com Saltos {}'.format(i))    
print('FIM ~ ex.03\n\n')

# Ex.04    
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int (input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM ~ ex.04')    