# Faça um programa que leia um número qualquer e mostre o seu FATORIAL. Ex.: 5! = 5x4x3x2x1 = 120

print('\033[36m-=-'*10, 'FATORIAL', '-=-'*10, '\033[m')
num = int(input('Insira um Número: '))

# 01 Metodo (com a função FACTORIAL):
'''from math import factorial
f = factorial(num)
print('>>> {}! = {}'.format(num, f))'''

# 02 Metodo (com WHILE):
i = num
f = 1
print('>>> {}! = '.format(num), end='')
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ',end='')
    f *= i # equivalente : f = f * i
    i -= 1 # equivalente : i = i - 1
print('{}'.format(f))    

# 03 Metodo (com FOR):
'''f = 1
print('>>> {}! = '.format(num), end='')
for i in range (num, 0, -1) :
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ',end='')
    f *= i 
print('{}'.format(f))'''