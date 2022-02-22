# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usúario qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10, e R$1.

print(f'='*25,'\n\tBACO CEV\n','='*25)
saque = int(input('Quanto quer sacar? R$'))
total = saque
total_cedula = 0
cedula = 50 # maior valor 

while True:
    if total >= cedula:
        total -= cedula 
        total_cedula += 1 # contagem do numero de cedulas 
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}.')
        # Alteração dos valores da cedulas:    
        if cedula == 50:
            cedula = 20 # proxima cedula 
        elif cedula == 20:
            cedula = 10 # proxima cedula 
        elif cedula == 10:
            cedula = 1 # proxima cedula 

        total_cedula = 0 # reinicializando 
        if total == 0: # Condição de parada 
            break
