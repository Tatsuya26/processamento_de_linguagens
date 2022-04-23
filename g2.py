
import re
import sys

'''
    a   =     34 +   23  -  7   *   2

    ID ATRIB INT OP INT OP INT OP INT

'''
id = r'[_A-Za-z]\w*'

iss = r'\d+'

#automato finito determinista
#afd = (s, z, Estados , funcaoTransicao)

'''
        d       _       letra
-----------------------------
S       B       A         A
B       B       -         -
A       A       A         A

incial = s
final  = b 
estado  = inicial


for token in input:
    estado = tabela[estado,t]

if estado in final:
    sucesso
'''

def tokenize(code):
    token_specification = [
        ('NUM', r'\d+'), #inteiro sem sinal
        ('ATRIB',r'=' ), #assign
        ('ID'   , r'[_A-Za-z]\w*'), #identificadores
        ('OP'   , r'[+|-*/'),     #operation
        ('NEWLINE', r'\n'), 
        ('SKIP',    r'[ \t]+'),
        ('ERRO', r'.')
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    reconhecidos = []
    mo = re.finditer(tok_regex,code)
    for m in mo:
        dic = m.groupdict()
        print(dic)
        reconhecidos.append(m)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)