# Curso em Video - Curso de Python 3 - aula15
# Interrompendo Repetilções While com o BREAK

# Ex. 01:
soma = 0 
while True:   # Loop Infinito
    n = int(input('Insira um Número: [999 - Sair] ')) 
    if n == 999:
        break   # Interrupção (quebra o loop)
    soma += n
print(f'A soma é {soma}') #print('Soma = {}'.format(soma))  # ATUALIZAÇÃO DO PYTHON 3.6  ou superior  