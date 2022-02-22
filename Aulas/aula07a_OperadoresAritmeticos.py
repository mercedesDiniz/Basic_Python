# Curso em Video - Curso de Python 3 - aula07A

# Operadores Aritméticos:                  | Ordem de Procedência:   
# (+) adição; (-) subtração;               | 1. ()
# (*) multiplicação; (/) divisão;          | 2. **
# (**) potência; (//) divisão inteira;     | 3. *, /, //, %
# (%) modulo ou resto da divisão           | 4. +, -
# (==) igual à                             |

n1 = int(input('Valor um: '))
n2 = int(input('Valor dois: '))
som = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('Soma: {}; Subtração: {}; Multiblicação: {}'.format(som, sub, m), end=' ')
print('Divisão: {:.3f}; Divisão Inteira: {};\n Potência: {}'.format(d, di, e))
