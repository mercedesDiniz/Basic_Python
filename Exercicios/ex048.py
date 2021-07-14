# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500. 
 
soma = 0 # acumulador
cont = 0 # contador
for i in range(1, 501, 2):
    if i%3 == 0:
        soma +=  i 
        cont +=  1

print('A Soma de todos os {} valores solicitado é {}! '.format(cont, soma))
