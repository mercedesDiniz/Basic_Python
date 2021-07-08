# Refaça o DEsafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado. EQUILÁTERO,ISÓCELES e ESCALENO

print('\033[34m-=\033[m'*30)
print('\033[36mANALIZADOR DE TRIANGULOS')
r1 = float(input('Insira o comprimento da Reta01: '))
r2 = float(input('Insira o comprimento da Reta02: '))
r3 = float(input('Insira o comprimento da Reta03: '))
print('\033[34m-=\033[m'*30)

if r1 < r2+r3 and r2 < r1+r3 and r3 <r1+r2 :
    print('\033[32mEssas Retas podem Forma um Triangulo! \033[m', end='')
    if r1 == r2 == r3 :      
        print('\033[33mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1 :
        print('\033[33mESCALENO\033[m')
    else:
        print('\033[33mISÓCELES\033[m')
else:
    print('\033[31mEssas Retas NÃO podem Forma um Triangulo!\033[m')        
   