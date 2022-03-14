#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas; - A maior nota; - A menor nota; - A média da turma; - A situação (opcional). Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(* n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (ACEITA VARIAS)
    :param sist: (opcional), indica se deve adicionar a situação
    :return: dicionáruio com vàrias informações sobre a situação da turma
    '''
    resposta = []   


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)