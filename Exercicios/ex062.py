# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('=-=-=-=-=-= GERADOR DE PA =-=-=-=-=-=')
primeiro_termo = int(input('Insira o Primeiro Termo da PA: '))
razao = int(input('Insira a Razão da PA: '))

termo = primeiro_termo
contador = 1
totalDeTermos = 0
mais_termos = 10


while mais_termos != 0:
    totalDeTermos = totalDeTermos + mais_termos
    while contador <= totalDeTermos:
        print('{} '.format(termo), end='-> ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Deseja mais quantos termos? '))
print('FIM')
print('Progressao Finalizada com {} termos mostrados.'.format(totalDeTermos))