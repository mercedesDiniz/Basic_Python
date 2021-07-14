# Curso em Video - Curso de Python 3 - aula08
# https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLpwygc0AuGOXJ18fPwPNIeXvzKid_AUkm&index=23

# Utilizando Módulos: para incluir alguma coisa utilizamos os comandos: 
# "import nomeDaBiblioteca" para importar todas as funcionalidades de um móduo
# "from nomeDaBiblioteca import nomeEspecifico1, nomeEspecifico2"  para importar apenas as funcionalidades especificadas

# Documentação do 3.8.10: https://docs.python.org/pt-br/3.8/library/index.html
 
# Biblioteca   | Funções
#    math      | ceil, floor, trunc, pow, sqrt, factorial

# import math  # importando toda a biblioteca de matematica
from math import sqrt, ceil, floor
num = int(input('Insira um numero: '))

raiz = sqrt(num)  # ou math.sqrt(num) se importa toda a math
print('A raiz quadrada de {} é igual a {:.3f}'.format(num, raiz))
print('Arredondado para cima: {}\nArredondado para baixo: {}'.format(ceil(raiz), floor(raiz)))