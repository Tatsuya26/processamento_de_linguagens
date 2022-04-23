import ply.lex as lex
import ply.yacc as yacc

import sys

tokens = ["NUM", "PAL"]
literals = ["[","]", ","]

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
#def p_grammar(p):
#    """
#    lista : '[' conteudo ']'
#
#    conteudo : 
#             | elementos
#
#    elementos : elem
#              | elem ',' elementos
#
#    elem : PAL 
#         | NUM 
#    """

#funcionam as duas versões mas recursividade à esquerda é mais eficiente(?)

def p_lista(p):
    "lista : '[' conteudo ']'"

def p_conteudo_vazio(p):
    "conteudo : "

def p_conteudo_elementos(p):
    "conteudo : elementos"

def p_elementos_um(p):
    "elementos : elem"

def p_elementos_lista(p):
    "elementos : elementos ',' elem"

def p_elem_num(p):
    "elem : NUM"
    print("Encontrei um número")
    p.parser.contador_nums =+1

def p_elem_pal(p):
    "elem : PAL"
    print("Encontrei uma palavra")
    p.parser.contador_pals = + 1

def p_elem_lista(p):
    "elem : lista"


def p_error(p):
    print("Sintax error")

parser = yacc.yacc()
parser.contador_nums = 0    
parser.contador_pals = 0
p = 0
# yacc é bottom-up

for line in sys.stdin:
    parser.parse(line)
    print("Encontrei " + str(parser.contador_pals) + " palavras")
