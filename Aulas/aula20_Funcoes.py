# Curso em Video - Curso de Python 3 - aula20
# Variáveis Compostas: FUNÇÔES - Parte 1
# Link: https://www.youtube.com/watch?v=ezfr9d7wd_k&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=29

'''Funções são blocos de código (e uma rotinas personalizada) identificados por um nome, que podem receber parâmetros pré-determinados.
# Caracteristicas:
    - Podem retornar ou não objetos;
    - Aceitam DocStrings (são strings que estão associadas a uma estrutura e servem de documentação);
    - Aceitam parâmetros opcionais (com defaults);
    - Aceitam que os parâmetros sejam passados com nome;
    - Tem namespace próprio (escopo local).  '''

# Criando uma função:
'''
def nomefunc(parametro1, parametro2=padrao):
"""DocString
"""
<bloco de código>
return valor '''

# Ex.01: Criando algumas Funções
from turtle import pos


def mostraLinha(tipo = '-', x = 30): # definição da função
    print(str(tipo)*x) # bloco de instruções

def tituloFormatado(msg): # definição da função
    mostraLinha()
    print(f'{msg.upper():^30}')
    mostraLinha()


# Usando as funções:
mostraLinha() # com os valores padrao
mostraLinha('-*-', 20) # com parametros
tituloFormatado('Teste função') # usando a função

# Ex.02: Empacotando Parametros
def contT(* num): # * -> siguinifica desempacotar
    # argumentos são recebidos na forma de uma TUPLA
    print(f'Recebido os valores {num}, e são {len(num)} elementos.')

contT(2, 1, 7)
contT(0, 8)
contT(1, 2, 3, 4, 5, 6)

# Ex.03: Usando Listas
def dobro(lst):
    i = 0 
    while i < len(lst):
        lst[i] *= 2
        i += 1
    print(f'Dobro: {lst}')

valores = [1, 2, 3, 4, 5, 6]
dobro(valores)