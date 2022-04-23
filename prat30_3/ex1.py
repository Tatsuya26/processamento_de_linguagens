from tokenize import String
import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = ["NUM","START","END"]
literals = ["[","]", ","]

t_NUM = r"\d+"
t_START = r"start"
t_END   = r"end"

t_ignore = " \n\t\r"

def t_error(t):
    print("Error")
    lexer.skip(1)

lexer = lex.lex()

def p_Lista(p):
    "Lista : '[' conteudo ']'"

def p_conteudo_vazio(p):
    "conteudo : "

def p_conteudo_elementos(p):
    "conteudo : Elementos"

def p_Elementos(p):
    "Elementos : Elem ',' Elementos"

def p_Elementos_Elem(p):
    "Elementos : Elem"

def p_Elem_Num(p):
    "Elem : NUM"
    if(parser.start_flag):
        parser.soma += int(p[1])
    parser.len += 1


def p_Elem_end(p):
    "Elem : END"
    parser.start_flag = False
    parser.len += 1
    print("Pretende imprimir o valor acumulado?")
    str = input()
    if str == "yes":
        print("Soma actual = " + str(parser.soma))
    


def p_Elem_start(p):
    "Elem : START"
    parser.start_flag = True
    parser.len += 1

parser = yacc.yacc()
parser.len = 0
parser.start_flag = False
parser.soma = 0

for line in sys.stdin:
    parser.parse(line)
    print(parser.len)
    print("Soma start to end = " + str(parser.soma))