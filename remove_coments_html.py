import ply.lex as lex, sys

states = [('COM','exclusive')]

tokens = [  "BCOM","ECOM","PRINT"]

def t_BCOM(t):
    r'<!--'
    t.lexer.begin("COM")
    return t

def t_COM_ECOM(t):
    r'-->'
    t.lexer.begin("INITIAL")
    return t

def t_ANY_error(t):
    print("Este token nao e reconhecido",t.value)
    t.lexer.skip(1)

def t_PRINT(t):
    r'.|\n'
    print(t.value, end = "")
    return t

def t_COM_PRINT(t):
    r'.|\n'
    pass

lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        pass
    
