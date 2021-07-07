# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com ela: Até 9 anos é MIRIN, até 14 anos é INFANTIL, até 19 anos é JUNIOR, até 20 anos é SÊNIOR e acima é MASTER.

from datetime import date
print('\033[1;34m-=-\033[m'*30)
print('\033[1;36mAVALIANDO CATEGORIA\033[m')
ano_nascimento = int(input('Insira o Ano de Nascimento: '))
ano_atual = date.today().year  # Vai pega só o ano da data atual
idade = ano_atual - ano_nascimento
print('Se enquadra na Categoria :')
if idade <= 9 :
    print('\033[36mMIRIN\033[m')
elif idade > 9 and idade <= 14 :
    print('\033[36mINFANTIL\033[m')
elif idade > 14 and idade <= 19 :
    print('\033[36mJUNIOR\033[m')
elif idade > 19 and idade <= 20 :
    print('\033[36mSÊNIOR\033[m')
else:
    print('\033[36mMASTER\033[m')  

print('\033[1;34m-=-\033[m'*30)    