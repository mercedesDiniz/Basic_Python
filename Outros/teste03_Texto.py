'''O módulo também implementa um tipo chamado Template, que é um modelo de string que pode ser preenchido através de um dicionário. Os identificadores são inciados por cifrão ($) e podem ser cercados por chaves, para evitar confusões.'''
# Ex.01:
import string # importando o módulo string
st = string.Template('$aviso aconteceu em $quando') # Cria uma string template

# Preenche o modelo com um dicionário:
s = st.substitute({'aviso': 'Falta de eletricidade',
'quando': '03 de Abril de 2002'})

print (s) # mostra "Falta de eletricidade aconteceu em 03 de Abril de 2002"
g.MutableString('Python')
s[0] = 'p'
print (s) # mostra "python" '''
'''Strings mutáveis são menos eficientes do que strings imutáveis, pois são mais complexas (em termos de estrutura), o que se reflete em maior consumo de recursos (CPU e memória). '''
