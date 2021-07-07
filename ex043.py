# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
#  - Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso ideal; De 25 até 30: Sobrepeso; De 30 até 40: Obesidade; Acima de 40: Obesidade Moŕbida.

from math import pow
peso = float(input('Insira o seu Peso (em Kg): '))
altura = float(input('Insira a sua Altura (em metros): '))

imc = peso/(pow(altura, 2))

if imc < 18.5 :
    print('\033[31m ABAIXO DO PESO\033[m') 
elif imc >= 18.5 and imc < 25 :
    print('\033[32m PESO IDEAL\033[m') 
elif imc >= 25 and imc < 30 :
    print('\033[33m SOBREPESO\033[m')  
elif imc >= 30 and imc < 40 :
    print('\033[31m OBESIDADE\033[m') 
elif imc >=40 :
    print('\033[31m OBESIDADE MORBIDA\033[m')           