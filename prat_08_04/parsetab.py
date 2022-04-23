
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "textoDir : '(' texto Conteudo ')'Dir : FicheiroConteudo : Conteudo DirConteudo : Ficheiro : '[' texto texto ']'"
    
_lr_action_items = {'(':([0,3,5,7,9,10,11,],[2,-2,-4,2,-1,-3,-5,]),'[':([0,3,5,7,9,10,11,],[4,-2,-4,4,-1,-3,-5,]),'$end':([1,3,9,11,],[0,-2,-1,-5,]),'texto':([2,4,6,],[5,6,8,]),')':([3,5,7,9,10,11,],[-2,-4,9,-1,-3,-5,]),']':([8,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Dir':([0,7,],[1,10,]),'Ficheiro':([0,7,],[3,3,]),'Conteudo':([5,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Dir","S'",1,None,None,None),
  ('Dir -> ( texto Conteudo )','Dir',4,'p_Dir','dir.py',13),
  ('Dir -> Ficheiro','Dir',1,'p_Dir_Ficheiro','dir.py',18),
  ('Conteudo -> Conteudo Dir','Conteudo',2,'p_Conteudo','dir.py',24),
  ('Conteudo -> <empty>','Conteudo',0,'p_Conteudo_vazio','dir.py',29),
  ('Ficheiro -> [ texto texto ]','Ficheiro',4,'p_Ficheiro','dir.py',34),
]