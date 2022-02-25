# Crie um programa que tenha um tupla com várias palavras (não usar acentos). Depois disso, voce deve mostras, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'limguagem', 'python', 'curso', 'gratis',
'estudar','praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras: # analiza cada elementos da tupla
    print(f'\nNa palavra \033[33m{p.upper()}\033[m temos ', end='')
    for letra in p: # analiza cada letra da palavra
        if letra.lower() in 'aeiou':
            print(f'\033[33m{letra} \033[m', end='')
print()