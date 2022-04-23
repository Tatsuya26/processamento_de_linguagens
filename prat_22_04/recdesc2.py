# ------------------------------------------------------------
# recdesc.py
#
# Parser recursivo descendente para listas de inteiros:
# []
# [8]
# [4,5,6,7]
# ------------------------------------------------------------
import ply.lex as lex

literals = ['+','-','*','/','(',')','.','=']
tokens = ['num','id']

t_id    = r'[A-Za-z_]\w*'
t_num   = r'\d+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Erro léxico no token '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

###########################
prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro Sintático: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)


def rec_Termo2():
    global prox_simb
    if prox_simb == '*' :
        rec_term('*')
        rec_Termo()
    elif prox_simb == '/' :
        rec_term('/')
        rec_Termo()
    elif prox_simb.type in ['(','.','+','-']:
        pass
    else :
        parserError(prox_simb)

def rec_Fator():
    global prox_simb
    if prox_simb == 'id' :
        rec_term('id')
    elif prox_simb == 'num' :
        rec_term('num')
    elif prox_simb == '(':
        rec_term('(')
        rec_Exp()
        rec_term(')')
    else :
        parserError(prox_simb)

def rec_Termo():
    rec_Fator()
    rec_Termo2()

def rec_Exp2():
    global prox_simb
    if prox_simb == '+' :
        rec_term('+')
        rec_Exp()
    elif prox_simb == '-' :
        rec_term('-')
        rec_Exp()
    elif prox_simb.type in ['(','.',]:
        pass
    else :
        parserError(prox_simb)


def rec_Exp():
    rec_Termo()
    rec_Exp2()

def rec_Calc():
    rec_Exp()
    rec_term('.')


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Calc()
    print("That's the end...")


# Programa de teste
linha = input("Introduza uma lista: ")
# Teste do tokenizer
# lexer.input(linha)
# for tok in lexer:
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
rec_Parser(linha)
    



