# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se els podem ou não forma um triângulo.

print('\033[34m-=\033[m'*30)
print('\033[36mANALIZADOR DE TRIANGULOS')
r1 = float(input('Insira o comprimento da Reta01: '))
r2 = float(input('Insira o comprimento da Reta02: '))
r3 = float(input('Insira o comprimento da Reta03: '))
print('\033[34m-=\033[m'*30)

if r1 < r2+r3 and r2 < r1+r3 and r3 <r1+r2 :
    print('\033[32mEssas Retas podem Forma um Triangulo!\033[m')
else:
    print('\033[31mEssas Retas NÃO podem Forma um Triangulo!\033[m')        
   