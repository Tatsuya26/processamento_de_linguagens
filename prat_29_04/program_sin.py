import ply.yacc as yacc

from program_tokenizer import tokens, literals



def p_program(p):
    "Program : Declarations Statements"

def p_Declarations_List(p):
    "Declarations : Declarations Declaration"

def p_Declarations_empty(p):
    "Declarations : "

def p_Declaration(p):
    "Declaration : Type IdList"

def p_Type_str(p):
    "Type : STR"

def p_Type_int(p):
    "Type : INT"

def p_IdList_list(p):
    "IdList : IdList ',' id"

def p_IdList_single(p):
    "IdList : id"

def p_Statements_List(p):
    "Statements : Statements Statement"

def p_Statements_single(p):
    "Statements : Statement"

def p_Statement_a1trib(p):
    "Statement : id '=' Exp"

def p_Statement_print(p):
    "Statement : PRINT '(' PrintArgs ')'"

def p_PrintArgs_list(p):
    "PrintArgs : PrintArgs ',' PrintArg"

def p_PrintArgs_Single(p):
    "PrintArgs : PrintArg"

def p_Exp_id(p):
    "Exp : id"

def p_PrintArg_str(p):
    "PrintArg : str"

def p_PrintArg_exp(p):
    "PrintArg : Exp"

def p_Exp_INPUT(p):
    "Exp : INPUT '(' str ')'"

def p_Exp_INT(p):
    "Exp : INT '(' Exp ')'"

def p_Statement_if(p):
    "Statement : IF '(' Cond ')' CondStatements Else"

def p_Else_Empty(p):
    "Else :"

def p_Else_else(p):
    "Else : ELSE CondStatements"

def p_CondStatements_single(p):
    "CondStatements : Statement"

def p_CondStatements_composto(p):
    "CondStatements : '{' Statements '}'"

def p_Cond_or(p):
    "Cond : Cond OR Cond2"

def p_Cond(p):
    "Cond : Cond2"

def p_Cond2_and(p):
    "Cond2 : Cond2 AND Cond3"

def p_Cond2(p):
    "Cond2 : Cond3"

def p_Cond3_not(p):
    "Cond3 : NOT ExpRel"

def p_Cond3(p):
    "Cond3 : ExpRel"

def p_ExpRel_gt(p):
    "ExpRel : Exp '>' Exp"

def p_ExpRel_lt(p):
    "ExpRel : Exp '<' Exp"


def p_ExpRel_ge(p):
    "ExpRel : Exp GE Exp"

def p_ExpRel_le(p):
    "ExpRel : Exp LE Exp"

def p_ExpRel_eq(p):
    "ExpRel : Exp EQ Exp"

def p_ExpRel_neq(p):
    "ExpRel : Exp NEQ Exp"







def p_error(p):
    print("Erro sintatico ", p)
    parser.success = False






parser = yacc.yacc()

from sys import stdin
parser.success = True
program = stdin.read()
parser.parse(program)

if parser.success:
    print("Programa estruturalemente correto!")
else:
    print("Programa com erros... Corrija!")
