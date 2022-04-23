import ply.lex as lex
import ply.yacc as yacc

import sys

tokens = ["PA", "PF", "NUM", "PAL"]

t_PA = r"\["
t_PF = r"\]"
t_NUM = r"\d+"
t_PAL = r"[a-zA-Z]+"

t_ignore = " \n\t\r"

def t_error(t):
    print("Illegal character " + t.value[0])


lexer = lex.lex()

#analisador léxico
#for line in sys.stdin:
#    lexer.input(line)
#    for tok in lexer:
#        print(tok)

#analisador sintático


def p_grammar(p):
    """
    lista : PA elementos PF
    elementos : 
              | elem elementos
    elem : PAL 
         | NUM
    """

def p_error(p):
    print("Sintax error")

parser = yacc.yacc()

for line in sys.stdin:
    parser.parse(line)