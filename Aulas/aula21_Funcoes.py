# Curso em Video - Curso de Python 3 - aula21
# Variáveis Compostas: FUNÇÔES - Parte 2
# Link: https://www.youtube.com/watch?v=etjJ_4Eqrk8&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=35


# Interactive Help - Ajuda Interativa
''' consultar a documentação no próprio interpretador (q - valtar quit - sair) '''
# help() 
# print(nome_Funcao.__doc__)

# DocStrings 
''' são strings que estão associadas a uma estrutura e servem de documentação, colocadas dentro do corpo da função, geralmente no começo'''
# Ex.01:
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :returm: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('.')

contador(2, 10, 2)
# help(contador)


# Parâmetros Opcionais
# Ex.02:
def somar_numeros(a=0, b=0, c=0):
    """
    -> Faz a soma de até três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor

    """
    s = a + b + c
    print(f'{a} + {b} + {c} = {s}')

somar_numeros(3, 2, 5)
somar_numeros(8, 4)
somar_numeros(b=3, c=6)
somar_numeros(4)
somar_numeros()


# Escopo de Variáveis/Declarações - É o local enque a variavel vai existir/ou não dentro do programa
# Ex.03:
def teste1(b):
    a = 8 # É criado uma outra variavel. Ela é local e diferente na "a" global 
    print(f'\nTeste01:\n- "A" dentro (local) vale {a}')

a = 5
teste1(a)
print(f'- "A" fora (global) vale {a}')

def teste2(b):
    global a # associa/usa a variavel "a" global 
    a = 8
    print(f'Teste02:\n- "A" dentro (local) vale {a}')

a = 5
teste2(a)
print(f'- "A" fora (global) vale {a}')


# Retorno de valores - return()
# Ex. 04:
def somar_numeros2(a=0, b=0, c=0):
    s = a + b + c
    return s 

r1 = somar_numeros2(3, 2, 5)
r2 = somar_numeros2(b=3, c=6)
r3 = somar_numeros2(8, 4)
print(f'\nRetornos: {r1}, {r2} e {r3}.')