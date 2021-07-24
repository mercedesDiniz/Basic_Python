# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada vaor digitado pelo usuário. Oprograma será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Quer ver a Tabuada de qual número? '))
    if n<0 :
        break
    print('-'*45)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-'*45)
print('FIM!')    