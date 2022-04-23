
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NUM PAL\n    lista : '[' conteudo ']'\n\n    conteudo :\n             | elementos\n\n    elementos : elem\n              | elem ',' elementos\n\n    elem : NUM\n         | PAL\n         | lista\n\n    "
    
_lr_action_items = {'[':([0,2,10,],[2,2,2,]),'$end':([1,9,],[0,-1,]),']':([2,3,4,5,6,7,8,9,11,],[-2,9,-3,-4,-6,-7,-8,-1,-5,]),'NUM':([2,10,],[6,6,]),'PAL':([2,10,],[7,7,]),',':([5,6,7,8,9,],[10,-6,-7,-8,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista':([0,2,10,],[1,8,8,]),'conteudo':([2,],[3,]),'elementos':([2,10,],[4,11,]),'elem':([2,10,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista","S'",1,None,None,None),
  ('lista -> [ conteudo ]','lista',3,'p_grammar','mlistas.py',21),
  ('conteudo -> <empty>','conteudo',0,'p_grammar','mlistas.py',23),
  ('conteudo -> elementos','conteudo',1,'p_grammar','mlistas.py',24),
  ('elementos -> elem','elementos',1,'p_grammar','mlistas.py',26),
  ('elementos -> elem , elementos','elementos',3,'p_grammar','mlistas.py',27),
  ('elem -> NUM','elem',1,'p_grammar','mlistas.py',29),
  ('elem -> PAL','elem',1,'p_grammar','mlistas.py',30),
  ('elem -> lista','elem',1,'p_grammar','mlistas.py',31),
]
