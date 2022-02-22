# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Insira o nome da Cidade: ')).strip()

cidade = cidade.upper()
cidade = cidade.split() # divisão considerando os espaços, gera um lista com todas as palavra de um cadeia de caracteres
print(' Esse começa com "Santo"? {}'.format('SANTO' in cidade[0])) # ou cidade[:5] == 'SANTO'