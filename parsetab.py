
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA EQUALS EQUALS_EQUALS FOR HEADER ID INCLUDE INCREMENT INT LBRACE LEQ LPAREN MULT NUMBER PLUS RBRACE RETURN RPAREN SEMICOLON\n    program : include main_function\n    \n    include : INCLUDE HEADER\n    \n    main_function : INT ID LPAREN RPAREN LBRACE statements RBRACE\n    \n    statements : statement statements\n                | statement\n    \n    statement : declaration SEMICOLON\n                | assignment SEMICOLON\n                | for_loop\n                | RETURN expression SEMICOLON\n                | expression SEMICOLON\n    \n    declarations : declaration SEMICOLON declarations\n                | declaration SEMICOLON\n    \n    declaration : type ID EQUALS expression \n    | declaration\n    \n    type : INT\n    \n    for_loop : FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN LBRACE statements RBRACE\n    \n    assignment : ID EQUALS expression\n    \n    condition : ID LEQ NUMBER\n    \n    increment : ID INCREMENT\n    \n    expression : NUMBER\n                | ID\n                | expression PLUS expression\n                | ID MULT NUMBER\n    '
    
_lr_action_items = {'INCLUDE':([0,],[3,]),'$end':([1,4,25,],[0,-1,-3,]),'INT':([2,6,10,14,17,27,28,31,37,53,55,],[5,-2,11,11,-8,-6,-7,-10,-9,11,-16,]),'HEADER':([3,],[6,]),'ID':([5,10,11,14,17,18,20,23,27,28,31,32,34,37,39,43,46,53,55,],[7,12,-15,12,-8,30,33,30,-6,-7,-10,30,41,-9,30,45,49,12,-16,]),'LPAREN':([7,21,],[8,34,]),'RPAREN':([8,48,52,],[9,51,-19,]),'LBRACE':([9,51,],[10,53,]),'RETURN':([10,14,17,27,28,31,37,53,55,],[18,18,-8,-6,-7,-10,-9,18,-16,]),'FOR':([10,14,17,27,28,31,37,53,55,],[21,21,-8,-6,-7,-10,-9,21,-16,]),'NUMBER':([10,14,17,18,23,24,27,28,31,32,37,39,47,53,55,],[22,22,-8,22,22,36,-6,-7,-10,22,-9,22,50,22,-16,]),'EQUALS':([12,33,41,],[23,39,23,]),'SEMICOLON':([12,15,16,19,22,29,30,35,36,38,40,42,44,50,],[-21,27,28,31,-20,37,-21,-17,-23,-22,43,-13,46,-18,]),'PLUS':([12,19,22,29,30,35,36,38,42,],[-21,32,-20,32,-21,32,-23,32,32,]),'MULT':([12,30,],[24,24,]),'RBRACE':([13,14,17,26,27,28,31,37,54,55,],[25,-5,-8,-4,-6,-7,-10,-9,55,-16,]),'LEQ':([45,],[47,]),'INCREMENT':([49,],[52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'include':([0,],[2,]),'main_function':([2,],[4,]),'statements':([10,14,53,],[13,26,54,]),'statement':([10,14,53,],[14,14,14,]),'declaration':([10,14,53,],[15,15,15,]),'assignment':([10,14,34,53,],[16,16,40,16,]),'for_loop':([10,14,53,],[17,17,17,]),'expression':([10,14,18,23,32,39,53,],[19,19,29,35,38,42,19,]),'type':([10,14,53,],[20,20,20,]),'condition':([43,],[44,]),'increment':([46,],[48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> include main_function','program',2,'p_program','parser.py',15),
  ('include -> INCLUDE HEADER','include',2,'p_include','parser.py',22),
  ('main_function -> INT ID LPAREN RPAREN LBRACE statements RBRACE','main_function',7,'p_main_function','parser.py',29),
  ('statements -> statement statements','statements',2,'p_statements','parser.py',36),
  ('statements -> statement','statements',1,'p_statements','parser.py',37),
  ('statement -> declaration SEMICOLON','statement',2,'p_statement','parser.py',47),
  ('statement -> assignment SEMICOLON','statement',2,'p_statement','parser.py',48),
  ('statement -> for_loop','statement',1,'p_statement','parser.py',49),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_statement','parser.py',50),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','parser.py',51),
  ('declarations -> declaration SEMICOLON declarations','declarations',3,'p_declarations','parser.py',57),
  ('declarations -> declaration SEMICOLON','declarations',2,'p_declarations','parser.py',58),
  ('declaration -> type ID EQUALS expression','declaration',4,'p_declaration','parser.py',68),
  ('declaration -> declaration','declaration',1,'p_declaration','parser.py',69),
  ('type -> INT','type',1,'p_type','parser.py',84),
  ('for_loop -> FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN LBRACE statements RBRACE','for_loop',11,'p_for_loop','parser.py',91),
  ('assignment -> ID EQUALS expression','assignment',3,'p_assignment','parser.py',98),
  ('condition -> ID LEQ NUMBER','condition',3,'p_condition','parser.py',106),
  ('increment -> ID INCREMENT','increment',2,'p_increment','parser.py',113),
  ('expression -> NUMBER','expression',1,'p_expression','parser.py',121),
  ('expression -> ID','expression',1,'p_expression','parser.py',122),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',123),
  ('expression -> ID MULT NUMBER','expression',3,'p_expression','parser.py',124),
]
