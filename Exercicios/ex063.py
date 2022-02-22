# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de FIBONACCI. Ex. 0-> 1-> 1-> 2-> 3-> 5-> 8

print('\033[34m-=-'*5, '\033[36m SEQUÊNCIA DE FIBONACCI \033[m', '\033[34m--=-'*5, '\033[m')
n = int(input('Quantos termos voce quer vê? '))

t1 = 0 # termos iniciais fixos (de acordo com a teoria)
t2 = 1
contador = 3 # começa do 3 , pq o primeiro e o segundo ja foram
print('~'*50)
print('{} -> {}'.format(t1, t2), end='')
while contador <= n:
    t3 = t1 + t2 
    print(' -> {}'.format(t3), end='')
    t1 = t2  # deslocando os termos
    t2 = t3    
    contador += 1
print(' -> FIM')    
print('~'*50)