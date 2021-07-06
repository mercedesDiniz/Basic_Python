# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

v = float(input('Qual a sua Velocidade em Km/h? '))
if v > 80.00 :
    multa = (v-80.00) * 7
    print('\033[31mVoce foi Multado!Voce excedeu o limite de 80Km/h.\nValor à pagar é R${}.\033[m'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')