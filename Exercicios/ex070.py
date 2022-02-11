# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usúario vai continuar. No final, mostre: a) Qual é o total gasto na compra. b) Quantos produtos custão mais de R$1000. c) Qual é o nome do produto mais barato. 

total = Qtd_produtos1000 = 0
nomeProd_maisBarato = '...'

print('-'*40,'\n','{:^40}'.format('LOJA SUPER NIX'),'\n','-'*40)

while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))

    if total == 0 or preço < preçoProd_maisBarato:
        preçoProd_maisBarato = preço
        nomeProd_maisBarato = nome_produto

    total += preço
    
    if preço > 1000:
        Qtd_produtos1000 += 1 

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    print('-'*40)
    if continuar == 'N':
        break

print('{:-^40}'.format('FIM DA COMPRA'))
print(f'''
Total na Compra: R${total:.2f}
Qtd de Prod que custaram + de R$1000: {Qtd_produtos1000} 
Produto Mais Barato: {nomeProd_maisBarato} por R${preçoProd_maisBarato:.2f}
''')