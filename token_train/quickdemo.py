import ply.lex as lex

# Definição dos tokens
tokens =["ABRIR","NUMERO","SEPARADOR","FECHAR"]
 # [1,2,0,a,b,c,fim,3]
 # [1,a,b,0,fim] [A-Za-z]+
 # se encontrar 0 posso escrever palavras
 # qd encontrar "fim" ja nao posso escrever
 # <> asdasd </>
# Definição do reconhecimento dos tokens apenas com regex
t_FECHAR = '\]'
t_SEPARADOR = ','
# Definição do reconhecimento dos tokens utilizando funcoes

# Definir os nossos estados
states = [("palavras",'inclusive')] # inclusive exclusive

def t_ABRIR (t):
    r'\['
    print("Encontrei um abrir",t.type,t.value)
    return t

def t_NUMERO (t):
    r'\d+'
    t.lexer.comp+=1
    if(int(t.value)==0):
        # passar para o estado das palavras
        t.lexer.begin("palavras")
    print("Encontrei um numero",t.type,t.value)
    return t
#t.type,t.value, t.lineno, t.lexpos
# Regras para ignorar

def t_palavras_NUMERO(t):
    r'[A-Za-z]+'
    ## passar para o estado inicial
    if(t.value=="fim"):
        t.lexer.begin("INITIAL")
    return t

t_ignore='\n\t '

# Tratamento de erros
def t_error(t):
    print("Este token nao e reconhecido",t.value)
    t.lexer.skip(1)

# Criar instância de lex
lexer = lex.lex()
lexer.comp = 0
# Alimentar o lexer
import sys
for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)
    print(lexer.comp)