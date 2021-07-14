# Refaça o desafio ex009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('{:=^50}'.format(' TRABUADA '))
num = int(input('Insira um número: '))

for i in range (0, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))