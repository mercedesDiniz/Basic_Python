# Faça um programa que tenha uma funçao chamada área, que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l*c
    print(f'A área de um terreno {l}x{c} é de {area}m².')


print('-'*30, '\n', f'{"CONTROLE DE TERRENOS":^30}','\n','-'*30)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)