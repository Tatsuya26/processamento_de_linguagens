import ply.lex as lex
import ply.yacc as yacc
import sys
import os

literals = ['(',')','[',']']
tokens = ["texto"]


t_ignore = " \n\t"


def t_error(t):
    t.lexer.skip(1)

def t_texto(t):
    r'\"[^"]+\"'
    return t
    
lexer = lex.lex()

def p_Dir(p):
    "Dir : '(' texto Conteudo ')'"
    p[0] = [f"mkdir {p[2]}", f"cd {p[2]}"] + p[3]
    return p

def p_Dir_Ficheiro(p):
    "Dir : Ficheiro"
    p[0] = [p[1]]
    return p 


def p_Conteudo(p):
    "Conteudo : Conteudo Dir"
    p[0] = p[1] + p[2]
    return p

def p_Conteudo_vazio(p):
    "Conteudo : "
    p[0] = ["cd .."]
    return p

def p_Ficheiro(p):
    "Ficheiro : '[' texto texto ']'"
    p[0] = f"cp {p[3]} {p[2]}" 
    return p

parser = yacc.yacc()

linhas = ""
for line in sys.stdin:
    linhas += line


parser.parse(linhas)

