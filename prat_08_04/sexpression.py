from tokenize import String
import ply.lex as lex
import ply.yacc as yacc
import sys

literals = ["+","*",'(', ')']
tokens = ["num"]

def p_Result(p):
    "Result : SExp"
    print(p[1])
    return p

def p_SExp_soma(p):
    "SExp : '(' '+' Lista ')'"
    for val in p[3]:
        p[0] += val
    print(parser.result)
    return p

def p_SExp_mult(p):
    "SExp : '(' '*' Lista ')'"
    for val in p[3]:
        p[0] *= val
    print(parser.result)
    return p

def p_SExp_num(p):
    "SExp : num "
    p[0] = p[1]
    return p

def p_Lista(p):
    "Lista : Lista SExp"
    p[1].append(p[2])
    p[0] = p[1]
    return p

def p_Lista_SExp(p):
    "Lista : SExp SExp"
    p[0] = [p[1],p[2]]
    return p

lexer = lex.lex()
parser = yacc.yacc()


for line in sys.stdin:
    parser.parse(line)