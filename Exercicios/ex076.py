# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preções na sequencia. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Caderneta', 22.3, 'Livro', 34.9)

print('-'*40,)
print(f'{"LISTA DE PREÇOS":^40}\n', '-'*40)

for posicao in range (0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='') # p/ mostrar o nome do produto (estão em posiçoes pares)
    else:
        print(f'R${lista[posicao]:>7.2f}')

print('='*40,)