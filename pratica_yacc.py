import ply.lex as lex
import ply.yacc as yacc

tokens = ['NUM','OP']

t_NUM = r'\d+'
t_OP  = r'+|\-'
t_ignore = "\t\n "

def t_error(t):
    print("Este token nao é reconhecido", t.value)
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()

def p_Frase(p):
    "Frase : Elementos"

def p_Elementos(p):
    "Elementos : Elementos OP Elementos"
    if(p[2] == "+"):
        parser.output = int(p[1]) + int(p[2])
    else: 
        parser.output = int(p[1]) - int(p[2])
    print(p[1],p[2],p[3])

def p_Elementos_simples(p):
    "Elementos : Elemento"
    p[0] =p[1]

def p_Elemento(p):
    "Elemento : NUM"
    p[0] = p[1]

def p_error(p):
    print("Error" + p)
    parser.erro = True

parser = yacc.yacc()



import sys
for linha in sys.stdin:
    parser.output = 0
    parser.erro = False
    parser.parse(linha)
    
