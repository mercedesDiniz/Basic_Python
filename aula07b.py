# Alguns Alinhamentos basicos:
print('TESTE DE ALINHAMENTO')
nome = input('Digite algo:')
print('Centralizado :{:^20}'.format(nome))
print('Centralizado especial :{:=^20}'.format(nome))
print('Alinhado à Direita: {:>20}'.format(nome))
print('Alinhado à Esquerda: {:<20}'.format(nome))

# end=' ' -> para não quebrar a linha no final do prinf
# \n  -> para quebrar a linha 