
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND COMMENT ELSE EQ GE IF INPUT INT LE NEQ NOT OR PRINT STR id strProgram : Declarations StatementsDeclarations : Declarations DeclarationDeclarations : Declaration : Type IdListType : STRType : INTIdList : IdList ',' idIdList : idStatements : Statements StatementStatements : StatementStatement : id '=' ExpStatement : PRINT '(' PrintArgs ')'PrintArgs : PrintArgs ',' PrintArgPrintArgs : PrintArgExp : idPrintArg : strPrintArg : ExpExp : INPUT '(' str ')'Exp : INT '(' Exp ')'Statement : IF '(' Cond ')' CondStatements ElseElse :Else : ELSE CondStatementsCondStatements : StatementCondStatements : '{' Statements '}'Cond : Cond OR Cond2Cond : Cond2Cond2 : Cond2 AND Cond3Cond2 : Cond3Cond3 : NOT ExpRelCond3 : ExpRelExpRel : Exp '>' ExpExpRel : Exp '<' ExpExpRel : Exp GE ExpExpRel : Exp LE ExpExpRel : Exp EQ ExpExpRel : Exp NEQ Exp"
    
_lr_action_items = {'id':([0,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,30,33,35,36,37,38,39,40,42,43,44,45,46,47,51,52,53,62,63,64,65,66,67,68,],[-3,7,7,-2,-10,14,-5,-6,-9,-4,-8,19,19,19,33,-15,-11,19,-7,19,-12,19,7,19,19,19,19,19,19,19,19,-21,-23,7,-18,-19,-20,7,7,-22,-24,]),'PRINT':([0,2,3,4,5,12,13,14,19,20,33,36,38,51,52,53,62,63,64,65,66,67,68,],[-3,8,8,-2,-10,-9,-4,-8,-15,-11,-7,-12,8,-21,-23,8,-18,-19,-20,8,8,-22,-24,]),'IF':([0,2,3,4,5,12,13,14,19,20,33,36,38,51,52,53,62,63,64,65,66,67,68,],[-3,9,9,-2,-10,-9,-4,-8,-15,-11,-7,-12,9,-21,-23,9,-18,-19,-20,9,9,-22,-24,]),'STR':([0,2,4,13,14,33,],[-3,10,-2,-4,-8,-7,]),'INT':([0,2,4,13,14,15,16,17,30,33,35,37,39,40,42,43,44,45,46,47,],[-3,11,-2,-4,-8,22,22,22,22,-7,22,22,22,22,22,22,22,22,22,22,]),'$end':([1,3,5,12,19,20,36,51,52,62,63,64,67,68,],[0,-1,-10,-9,-15,-11,-12,-21,-23,-18,-19,-20,-22,-24,]),'}':([5,12,19,20,36,51,52,62,63,64,66,67,68,],[-10,-9,-15,-11,-12,-21,-23,-18,-19,-20,68,-22,-24,]),'=':([7,],[15,]),'(':([8,9,21,22,],[16,17,34,35,]),',':([13,14,19,23,24,25,26,33,50,62,63,],[18,-8,-15,37,-14,-16,-17,-7,-13,-18,-19,]),'INPUT':([15,16,17,30,35,37,39,40,42,43,44,45,46,47,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'str':([16,34,37,],[25,48,25,]),'NOT':([17,39,40,],[30,30,30,]),'ELSE':([19,20,36,51,52,62,63,64,67,68,],[-15,-11,-12,65,-23,-18,-19,-20,-22,-24,]),')':([19,23,24,25,26,27,28,29,31,41,48,49,50,54,55,56,57,58,59,60,61,62,63,],[-15,36,-14,-16,-17,38,-26,-28,-30,-29,62,63,-13,-25,-27,-31,-32,-33,-34,-35,-36,-18,-19,]),'>':([19,32,62,63,],[-15,42,-18,-19,]),'<':([19,32,62,63,],[-15,43,-18,-19,]),'GE':([19,32,62,63,],[-15,44,-18,-19,]),'LE':([19,32,62,63,],[-15,45,-18,-19,]),'EQ':([19,32,62,63,],[-15,46,-18,-19,]),'NEQ':([19,32,62,63,],[-15,47,-18,-19,]),'AND':([19,28,29,31,41,54,55,56,57,58,59,60,61,62,63,],[-15,40,-28,-30,-29,40,-27,-31,-32,-33,-34,-35,-36,-18,-19,]),'OR':([19,27,28,29,31,41,54,55,56,57,58,59,60,61,62,63,],[-15,39,-26,-28,-30,-29,-25,-27,-31,-32,-33,-34,-35,-36,-18,-19,]),'{':([38,65,],[53,53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Declarations':([0,],[2,]),'Statements':([2,53,],[3,66,]),'Declaration':([2,],[4,]),'Statement':([2,3,38,53,65,66,],[5,12,52,5,52,12,]),'Type':([2,],[6,]),'IdList':([6,],[13,]),'Exp':([15,16,17,30,35,37,39,40,42,43,44,45,46,47,],[20,26,32,32,49,26,32,32,56,57,58,59,60,61,]),'PrintArgs':([16,],[23,]),'PrintArg':([16,37,],[24,50,]),'Cond':([17,],[27,]),'Cond2':([17,39,],[28,54,]),'Cond3':([17,39,40,],[29,29,55,]),'ExpRel':([17,30,39,40,],[31,41,31,31,]),'CondStatements':([38,65,],[51,67,]),'Else':([51,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Declarations Statements','Program',2,'p_program','program_sin.py',8),
  ('Declarations -> Declarations Declaration','Declarations',2,'p_Declarations_List','program_sin.py',11),
  ('Declarations -> <empty>','Declarations',0,'p_Declarations_empty','program_sin.py',14),
  ('Declaration -> Type IdList','Declaration',2,'p_Declaration','program_sin.py',17),
  ('Type -> STR','Type',1,'p_Type_str','program_sin.py',20),
  ('Type -> INT','Type',1,'p_Type_int','program_sin.py',23),
  ('IdList -> IdList , id','IdList',3,'p_IdList_list','program_sin.py',26),
  ('IdList -> id','IdList',1,'p_IdList_single','program_sin.py',29),
  ('Statements -> Statements Statement','Statements',2,'p_Statements_List','program_sin.py',32),
  ('Statements -> Statement','Statements',1,'p_Statements_single','program_sin.py',35),
  ('Statement -> id = Exp','Statement',3,'p_Statement_a1trib','program_sin.py',38),
  ('Statement -> PRINT ( PrintArgs )','Statement',4,'p_Statement_print','program_sin.py',41),
  ('PrintArgs -> PrintArgs , PrintArg','PrintArgs',3,'p_PrintArgs_list','program_sin.py',44),
  ('PrintArgs -> PrintArg','PrintArgs',1,'p_PrintArgs_Single','program_sin.py',47),
  ('Exp -> id','Exp',1,'p_Exp_id','program_sin.py',50),
  ('PrintArg -> str','PrintArg',1,'p_PrintArg_str','program_sin.py',53),
  ('PrintArg -> Exp','PrintArg',1,'p_PrintArg_exp','program_sin.py',56),
  ('Exp -> INPUT ( str )','Exp',4,'p_Exp_INPUT','program_sin.py',59),
  ('Exp -> INT ( Exp )','Exp',4,'p_Exp_INT','program_sin.py',62),
  ('Statement -> IF ( Cond ) CondStatements Else','Statement',6,'p_Statement_if','program_sin.py',65),
  ('Else -> <empty>','Else',0,'p_Else_Empty','program_sin.py',68),
  ('Else -> ELSE CondStatements','Else',2,'p_Else_else','program_sin.py',71),
  ('CondStatements -> Statement','CondStatements',1,'p_CondStatements_single','program_sin.py',74),
  ('CondStatements -> { Statements }','CondStatements',3,'p_CondStatements_composto','program_sin.py',77),
  ('Cond -> Cond OR Cond2','Cond',3,'p_Cond_or','program_sin.py',80),
  ('Cond -> Cond2','Cond',1,'p_Cond','program_sin.py',83),
  ('Cond2 -> Cond2 AND Cond3','Cond2',3,'p_Cond2_and','program_sin.py',86),
  ('Cond2 -> Cond3','Cond2',1,'p_Cond2','program_sin.py',89),
  ('Cond3 -> NOT ExpRel','Cond3',2,'p_Cond3_not','program_sin.py',92),
  ('Cond3 -> ExpRel','Cond3',1,'p_Cond3','program_sin.py',95),
  ('ExpRel -> Exp > Exp','ExpRel',3,'p_ExpRel_gt','program_sin.py',98),
  ('ExpRel -> Exp < Exp','ExpRel',3,'p_ExpRel_lt','program_sin.py',101),
  ('ExpRel -> Exp GE Exp','ExpRel',3,'p_ExpRel_ge','program_sin.py',105),
  ('ExpRel -> Exp LE Exp','ExpRel',3,'p_ExpRel_le','program_sin.py',108),
  ('ExpRel -> Exp EQ Exp','ExpRel',3,'p_ExpRel_eq','program_sin.py',111),
  ('ExpRel -> Exp NEQ Exp','ExpRel',3,'p_ExpRel_neq','program_sin.py',114),
]
