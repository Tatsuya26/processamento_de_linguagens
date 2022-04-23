# ------------------------------------------------------------
# recdesc.py
#
# Parser recursivo descendente para listas de inteiros:
# []
# [8]
# [4,5,6,7]
# ------------------------------------------------------------
import ply.lex as lex
import sys

literals = ['+','-','*','/','(',')','.','=']
tokens = ['num','id','PRINT','READ','DUMP','END']


def t_PRINT(t):
    r'(?i)print'
    return t

def t_READ(t):
    r'(?i)read'
    return t

def t_DUMP(t):
    r'(?i) dump'
    return t

def t_END(t):
    r'(?i) end'
    return t


def t_num(t):
    r'\d+'
    return t;

def t_id(t):
    r'[A-Za-z_]\w*'
    return t;

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
    elif prox_simb.type in ['(','.','+','-','PRINT','READ','DUMP','id','DUMP']:
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
    elif prox_simb.type in ['(','.','PRINT','READ','DUMP','id','DUMP']:
        pass
    else :
        parserError(prox_simb)

def rec_Exp():
    rec_Termo()
    rec_Exp2()

def rec_Comando():
    global prox_simb
    if prox_simb == 'PRINT' :
        rec_term('PRINT')
        rec_Exp()
    elif prox_simb == '-' :
        rec_term('READ')
        rec_term('id')
    elif prox_simb == 'id':
        rec_term('id')
        rec_term('=')
        rec_Exp()
    elif prox_simb.type == 'DUMP':
        rec_term('DUMP')
    else :
        parserError(prox_simb)


def rec_Comandos():
    global prox_simb
    if prox_simb == 'END' :
        pass
    elif prox_simb.type in ['id','PRINT','READ','DUMP']:
        rec_Comando()
        rec_Comandos()
    else :
        parserError(prox_simb)

def rec_Calc():
    rec_Comando()
    rec_Comandos()
    rec_term('END')


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Calc()
    print("That's the end...")


# Programa de teste
linha = input("Introduza uma lista: ")
programa = sys.stdin.read()
# Teste do tokenizer
# lexer.input(linha)
# for tok in lexer:
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
rec_Parser(programa)
    




