
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "END NUM STARTLista : '[' conteudo ']'conteudo : conteudo : ElementosElementos : Elem ',' ElementosElementos : ElemElem : NUMElem : ENDElem : START"
    
_lr_action_items = {'[':([0,],[2,]),'$end':([1,9,],[0,-1,]),']':([2,3,4,5,6,7,8,11,],[-2,9,-3,-5,-6,-7,-8,-4,]),'NUM':([2,10,],[6,6,]),'END':([2,10,],[7,7,]),'START':([2,10,],[8,8,]),',':([5,6,7,8,],[10,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Lista':([0,],[1,]),'conteudo':([2,],[3,]),'Elementos':([2,10,],[4,11,]),'Elem':([2,10,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Lista","S'",1,None,None,None),
  ('Lista -> [ conteudo ]','Lista',3,'p_Lista','ex1.py',21),
  ('conteudo -> <empty>','conteudo',0,'p_conteudo_vazio','ex1.py',24),
  ('conteudo -> Elementos','conteudo',1,'p_conteudo_elementos','ex1.py',27),
  ('Elementos -> Elem , Elementos','Elementos',3,'p_Elementos','ex1.py',30),
  ('Elementos -> Elem','Elementos',1,'p_Elementos_Elem','ex1.py',33),
  ('Elem -> NUM','Elem',1,'p_Elem_Num','ex1.py',36),
  ('Elem -> END','Elem',1,'p_Elem_end','ex1.py',41),
  ('Elem -> START','Elem',1,'p_Elem_start','ex1.py',46),
]