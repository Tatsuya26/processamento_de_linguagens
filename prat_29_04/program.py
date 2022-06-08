'''
Program -> Declarations Statements
Declarations -> Declarations Declaration
                |
Declaration -> Type IdList

Type ->  INT
        | STR

IdList -> id
        | IdList ',' id


Statements -> Statements Statement
            |  Statement

Statement -> Atrib
            | Print
            | IF '(' Cond ')' CondStatements
            | IF '(' Cond ')' CondStatements Else

Else -> 
        | ELSE CondStatements

CondStatements -> Statement 
                | '{' Statements '}'

Cond -> Cond OR Cond2
        | Cond2

Cond2 -> Cond2 AND Cond3
        | Cond3

Cond3 -> NOT ExpRel
        |ExpRel
    
ExpRel  -> Exp '>' Exp
        | Exp '<' Exp
        | Exp GE Exp
        | Exp LE Exp
        | Exp EQ Exp
        | Exp NEQ Exp
        


Atrib -> id '=' Exp

Print -> PRINT '(' PrintArgs ')'

PrintArgs -> PrintArgs ',' PrintArg
            | PrintArg

PrintArg -> id
            | str
            | Exp

Exp -> INPUT '(' str ')'
     | INT '(' Exp ')'



'''