import ply.lex as lex

literals = ['(',')',',','=','>','<','{','}']
tokens = ['XML' ,'id']


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'



# Error handling rule
def t_error(t):
    print("Erro léxico no token '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()