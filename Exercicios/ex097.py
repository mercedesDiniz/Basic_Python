# Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))

escreva('T03')
escreva('Texto 01')
escreva('TextoTextoTextoTexto')