# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico

def leiaInt(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg)) # vai continuar pedindo um valor até ele ser válido
        # ANALISE:
        if n.isnumeric(): # caso seje um numero válido
            valor = int(n) # converte
            ok = True # condição p/ sair do laço
        else:
            print(f'\033[0;31mERRO! Digite o número inteiro válido.\033[m')
        if ok: # True
            break
    return valor
    

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')