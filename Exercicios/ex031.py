# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km p/ viagens de até 200Km e R$0,45 para viagens mais longas.


distancia = float(input('Qual é a Distancia da Viagem em Km? '))

'''if distancia <= 200.00 :
    preco = distancia*0.50
else:
    preco = distancia*0.45'''

preco = distancia * 0.50 if distancia <=200 else distancia * 0.45

print('Para um viagem de {}{:.2f}{} Km, sua passagem vai custar R$ {}{:.2f}{}.\nBoa Viagem!'.format('\033[33m',distancia,'\033[m','\033[33m',preco,'\033[m'))  
