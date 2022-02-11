# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('\033[36m-=-'*5, 'VOMOS JOGAR PAR ou IMPAR', '-=-'*5, '\033[m')
num_vitorias = 0

while True:
    num_computador = randint(0,10)
    num_jogador = int(input('Jogue um valor: '))
    op_jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    while op_jogador not in 'PpIi':
        op_jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    soma = num_computador + num_jogador
    if soma%2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'      

    print(f'\033[33mVoce jogou {num_jogador} e o Computador jogou {num_computador}.\nO Total é {soma}, que é {resultado}!\033[m') 

    if resultado[0] == op_jogador:
        print('\033[32mVOCE VENCEU !!!\033[m') 
        num_vitorias += 1
        print('-'*50)
    else:
        print('\033[31mVOCE PERDEU !!!\033[m')
        break

print(f'\033[31mGAME OVER!\033[m\nNúmero de Vitorias: {num_vitorias}')   