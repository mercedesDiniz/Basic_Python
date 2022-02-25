# Crie um programa onde o usuário digite uma expressão matematica qualquer que use parênteses. Seu aplicativo deverá analizar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Insira a expressão matemtica: '))

pilha = []
for elemento in expressao:
    if elemento == '(':
        pilha.append('(')
    elif elemento == ')':
        if len(pilha) > 0: # não vazia
            pilha.pop() # removendo o ultimo elementos
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'\033[32mExpressão Valida!\033[m\n>>> {expressao}')
else:
    print(f'\033[31mExpressão Invalida!\033[m\n>>> {expressao}')



'''# Obs.: Se estiver na ordem errada não detecta o erro. Ex: )5+4( 
if expressao.count('(') == expressao.count(')'):
    print(f'\033[32mExpressão Valida!\033[m\n>>> {expressao}')
else:
    print(f'\033[31mExpressão Invalida!\033[m\n>>> {expressao}')'''
