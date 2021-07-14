# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. (chatinho)

print('=-=-=-=-=-= 10 termos de uma PA =-=-=-=-=-=')
primeiro_termo = int(input('Insira o Primeiro Termo da PA: '))
razao = int(input('Insira a Razão da PA: '))

decimo_termo = primeiro_termo + (10-1) * razao

for termo in range(primeiro_termo, decimo_termo+razao, razao):
    print('{} '.format(termo), end='-> ')
print('ACABOU')  