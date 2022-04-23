import ply.lex as lex, sys, re


states = [("Feature","exclusive")]

tokens = [
    "B",
    "I",
    "O",
    ]

def t_B(t):
    r'B-.+'
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    t.lexer.tipo = partes[0]
    t.lexer.buffer = partes[1]
    lexer.begin("Feature")
    return t

def t_O(t):
    r'O.+'
    pass

def t_Feature_O(t):
    r'O.+'
    if t.lexer.tipo in t.lexer.features.keys():
        t.lexer.features[t.lexer.tipo].append(t.lexer.buffer)
    else :
        t.lexer.features[t.lexer.tipo] = [t.lexer.buffer]
    t.lexer.begin("INITIAL")


def t_Feature_I(t):
    r'I-.+'
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    t.lexer.buffer += " " + partes[1]
    pass

def t_Feature_B(t):
    r'B-.+'
    if t.lexer.tipo in t.lexer.features.keys():
        t.lexer.features[t.lexer.tipo].append(t.lexer.buffer)
    else :
        t.lexer.features[t.lexer.tipo] = [t.lexer.buffer]
    conteudo = t.value[2:]
    partes = re.split(r'\s+',conteudo)
    t.lexer.tipo = partes[0]
    t.lexer.buffer = partes[1]
    

def t_ANY_error(t):
    r'\n'
    t.lexer.skip(1)

lexer = lex.lex()
lexer.features = {}
lexer.tipo = ""
lexer.buffer = ""

for linha in sys.stdin:
    lexer.input(linha)
    for token in lexer:
        pass

print(lexer.features)
