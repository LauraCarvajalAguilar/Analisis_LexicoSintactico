# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIMPLEMENTSIMPORTleftCOMAleftAsignacionMasIgualMenosIgualMultiplicacionIgualDivisionIgualleftPuntoyComaleftORleftANDnonassocComparacionIgualDiferentenonassocSignoMenosMenorIgualMayorMayorIgualleftSignoMasSignoMenosleftELSErightCorcheteIzquierdarightPRIVATEPROTECTEDPUBLICFINALAND ARGS Asignacion BOOLEAN BREAK CADENADECARACTERES CARACTER CASE CATCHTRHOW CHAR CLASS COMA COMENTARIOS COMENTARIOSMULTILINEA ComillasDobles ComillasSimples ComparacionIgual CorcheteDerecha CorcheteIzquierda DEFAULT DO DOUBLE Diferente DivisionIgual DosPuntos ELSE EXTENDS FALSE FINAL FLOAT FOR IF IMPLEMENTS IMPORT INT Identificador LlaveDerecha LlaveIzquierda MAIN MasIgual MasMas Mayor MayorIgual Menor MenorIgual MenosIgual MenosMenos MultiplicacionIgual NEW Numero OR OUT PRINT PRINTLN PRIVATE PROTECTED PUBLIC ParentesisDerecho ParentesisIzquierdo Punto PuntoyComa RETURN STATIC STRING SWITCH SYSTEM SignoDividir SignoMas SignoMenos SignoMultiplicar TRUE TRY VOID WHILEprogram : PUBLIC CLASS Identificador LlaveIzquierda instrucciones  LlaveDerechainstrucciones : metodo_main LlaveIzquierda declaration_list LlaveDerecha\n\t\t\t\t\t | declaration_list\n\t\t\t\t\t metodo_main : PUBLIC STATIC VOID MAIN ParentesisIzquierdo STRING CorcheteIzquierda CorcheteDerecha ARGS ParentesisDerecho\n\t\t\t\t\tdeclaration_list : declaration_list  declaration\n   \t\t\t\t\t   | declaration \n\t\t\t\t\t   \n\t\t\t\t\t   \n   declaration : linea\n\t\t\t\t   | sentencia_while\n\t\t\t\t   | sentencia_iflinea : tipado PuntoyComa\n\t\t\t | mensaje PuntoyComa\n\t\t\t | modificadores PuntoyComa\n\t\t\t modificadores : PUBLIC tipado\n\t\t\t\t\t | PRIVATE tipado\n\t\t\t\t\t | PROTECTED tipadotipado : FLOAT assigment\n\t\t\t  | STRING Identificador Asignacion expression_cadena\n\t\t\t  | INT assigment \n\t\t\t  | DOUBLE assigment\n\t\t\t  | BOOLEAN assigment\n\t\t\t  | CHAR Identificador Asignacion expression_caractermensaje : SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena ParentesisDerecho\n\t\t\t   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo Identificador ParentesisDerecho \n\t\t\t   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena SignoMas expression ParentesisDerecho\n\t\t\t   | SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo ParentesisDerecho sentencia_while : DO LlaveIzquierda declaration_list LlaveDerecha cabecera_do_while PuntoyComa\n\t\t\t\t\t   | cabecera_while LlaveIzquierda declaration_list LlaveDerechasentencia_if : cabecera_if ELSE LlaveIzquierda declaration_list LlaveDerecha\n\t\t\t\t\t| cabecera_if ELSE cabecera_if\n\t\t\t\t\t| cabecera_ifcabecera_do_while : WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho\n\t\t\t\t         | WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerechocabecera_while : WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho\n\t\t\t\t        | WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerechocabecera_if : IF ParentesisIzquierdo expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerecha\n\t\t\t\t   | IF ParentesisIzquierdo double_expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerechaassigment : Identificador Asignacion expression   \n\t\t\t\t| Identificador MasIgual expression \n\t\t\t\t| Identificador MenosIgual expression \n\t\t\t\t| Identificador DivisionIgual expression\n\t\t\t\t| Identificadorexpression_cadena : CADENADECARACTERESexpression_caracter : CARACTERempty :double_expression_comparacion : expression_comparacion OR expression_comparacion\n\t\t\t\t\t\t\t\t\t | expression_comparacion AND expression_comparacionnumero_identificador : Numero\n\t\t\t\t\t\t\t| Identificadorexpression_comparacion : numero_identificador Diferente numero_identificador\n            \t               | numero_identificador Mayor numero_identificador\n            \t               | numero_identificador MayorIgual numero_identificador\n            \t               | numero_identificador Menor numero_identificador\n\t\t\t\t               | numero_identificador MenorIgual numero_identificador\n\t\t\t\t               | numero_identificador ComparacionIgual numero_identificador\n          \t\t               expression : expression SignoMas expression\n            \t   | expression SignoMenos expression\n            \t   | expression SignoMultiplicar expression\n            \t   | expression SignoDividir expression\n            \t   | ParentesisIzquierdo expression ParentesisDerecho\n          \t\t   | Numero\n\t\t\t\t   | Identificador'
    
_lr_action_items = {'PUBLIC':([0,5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[2,6,36,-6,-7,-8,-9,-30,36,-5,-10,-11,-12,36,36,36,36,36,-29,36,-27,36,-28,36,36,-26,36,36,-35,-36,]),'$end':([1,33,],[0,-1,]),'CLASS':([2,],[3,]),'Identificador':([3,10,21,22,23,24,25,53,54,62,63,64,65,84,93,94,96,97,98,99,100,101,108,109,110,111,126,132,147,],[4,37,45,45,45,45,49,72,72,82,82,82,82,82,72,72,72,72,72,72,72,72,82,82,82,82,72,140,82,]),'LlaveIzquierda':([4,8,18,19,43,92,95,102,103,151,],[5,34,41,42,61,-33,-34,122,123,-4,]),'DO':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[18,18,-6,-7,-8,-9,-30,18,-5,-10,-11,-12,18,18,18,18,18,-29,18,-27,18,-28,18,18,-26,18,18,-35,-36,]),'FLOAT':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[21,21,21,-6,-7,-8,-9,-30,21,21,21,-5,21,-10,-11,-12,21,21,21,21,21,-29,21,-27,21,-28,21,21,-26,21,21,-35,-36,]),'STRING':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,104,107,122,123,125,133,134,141,142,],[10,10,10,-6,-7,-8,-9,-30,10,10,10,-5,10,-10,-11,-12,10,10,10,10,10,-29,10,-27,10,124,-28,10,10,-26,10,10,-35,-36,]),'INT':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[22,22,22,-6,-7,-8,-9,-30,22,22,22,-5,22,-10,-11,-12,22,22,22,22,22,-29,22,-27,22,-28,22,22,-26,22,22,-35,-36,]),'DOUBLE':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[23,23,23,-6,-7,-8,-9,-30,23,23,23,-5,23,-10,-11,-12,23,23,23,23,23,-29,23,-27,23,-28,23,23,-26,23,23,-35,-36,]),'BOOLEAN':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[24,24,24,-6,-7,-8,-9,-30,24,24,24,-5,24,-10,-11,-12,24,24,24,24,24,-29,24,-27,24,-28,24,24,-26,24,24,-35,-36,]),'CHAR':([5,6,9,11,12,13,14,20,27,28,34,35,36,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[25,25,25,-6,-7,-8,-9,-30,25,25,25,-5,25,-10,-11,-12,25,25,25,25,25,-29,25,-27,25,-28,25,25,-26,25,25,-35,-36,]),'SYSTEM':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[26,26,-6,-7,-8,-9,-30,26,-5,-10,-11,-12,26,26,26,26,26,-29,26,-27,26,-28,26,26,-26,26,26,-35,-36,]),'PRIVATE':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[27,27,-6,-7,-8,-9,-30,27,-5,-10,-11,-12,27,27,27,27,27,-29,27,-27,27,-28,27,27,-26,27,27,-35,-36,]),'PROTECTED':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[28,28,-6,-7,-8,-9,-30,28,-5,-10,-11,-12,28,28,28,28,28,-29,28,-27,28,-28,28,28,-26,28,28,-35,-36,]),'WHILE':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,56,58,59,60,61,79,80,81,107,122,123,125,133,134,141,142,],[29,29,-6,-7,-8,-9,-30,29,-5,-10,-11,-12,29,29,29,29,29,-29,29,106,-27,29,-28,29,29,-26,29,29,-35,-36,]),'IF':([5,9,11,12,13,14,20,34,35,38,39,40,41,42,43,56,58,59,60,61,80,81,107,122,123,125,133,134,141,142,],[30,30,-6,-7,-8,-9,-30,30,-5,-10,-11,-12,30,30,30,30,30,30,-29,30,-27,30,-28,30,30,-26,30,30,-35,-36,]),'STATIC':([6,],[31,]),'LlaveDerecha':([7,9,11,12,13,14,20,35,38,39,40,56,58,59,60,76,80,81,107,125,133,134,141,142,],[33,-3,-6,-7,-8,-9,-30,-5,-10,-11,-12,76,79,80,-29,-2,-27,107,-28,-26,141,142,-35,-36,]),'PuntoyComa':([15,16,17,32,44,45,46,47,48,51,52,77,78,82,83,85,86,87,88,89,90,105,127,128,129,130,131,139,144,145,146,148,152,],[38,39,40,-13,-16,-41,-18,-19,-20,-14,-15,-17,-42,-61,-37,-60,-38,-39,-40,-21,-43,125,-55,-56,-57,-58,-59,-25,-31,-32,-22,-23,-24,]),'ELSE':([20,141,142,],[43,-35,-36,]),'Punto':([26,67,],[50,91,]),'ParentesisIzquierdo':([29,30,62,63,64,65,75,84,106,108,109,110,111,113,147,],[53,54,84,84,84,84,104,84,126,84,84,84,84,132,84,]),'VOID':([31,],[55,]),'Asignacion':([37,45,49,],[57,62,66,]),'MasIgual':([45,],[63,]),'MenosIgual':([45,],[64,]),'DivisionIgual':([45,],[65,]),'OUT':([50,],[67,]),'Numero':([53,54,62,63,64,65,84,93,94,96,97,98,99,100,101,108,109,110,111,126,147,],[71,71,85,85,85,85,85,71,71,71,71,71,71,71,71,85,85,85,85,71,85,]),'MAIN':([55,],[75,]),'CADENADECARACTERES':([57,132,],[78,78,]),'CARACTER':([66,],[90,]),'ParentesisDerecho':([68,69,71,72,73,74,78,82,85,112,114,115,116,117,118,119,120,121,127,128,129,130,131,132,136,137,138,140,149,150,],[92,95,-47,-48,102,103,-42,-61,-60,131,-45,-46,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,139,144,145,146,148,151,152,]),'OR':([68,71,72,73,116,117,118,119,120,121,136,],[93,-47,-48,93,-49,-50,-51,-52,-53,-54,93,]),'AND':([68,71,72,73,116,117,118,119,120,121,136,],[94,-47,-48,94,-49,-50,-51,-52,-53,-54,94,]),'Diferente':([70,71,72,],[96,-47,-48,]),'Mayor':([70,71,72,],[97,-47,-48,]),'MayorIgual':([70,71,72,],[98,-47,-48,]),'Menor':([70,71,72,],[99,-47,-48,]),'MenorIgual':([70,71,72,],[100,-47,-48,]),'ComparacionIgual':([70,71,72,],[101,-47,-48,]),'SignoMas':([78,82,83,85,86,87,88,112,127,128,129,130,131,138,150,],[-42,-61,108,-60,108,108,108,108,-55,108,108,108,-59,147,108,]),'SignoMenos':([82,83,85,86,87,88,112,127,128,129,130,131,150,],[-61,109,-60,109,109,109,109,-55,None,109,109,-59,109,]),'SignoMultiplicar':([82,83,85,86,87,88,112,127,128,129,130,131,150,],[-61,110,-60,110,110,110,110,-55,-56,110,110,-59,110,]),'SignoDividir':([82,83,85,86,87,88,112,127,128,129,130,131,150,],[-61,111,-60,111,111,111,111,-55,-56,111,111,-59,111,]),'PRINT':([91,],[113,]),'CorcheteIzquierda':([124,],[135,]),'CorcheteDerecha':([135,],[143,]),'ARGS':([143,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instrucciones':([5,],[7,]),'metodo_main':([5,],[8,]),'declaration_list':([5,34,41,42,61,122,123,],[9,56,58,59,81,133,134,]),'declaration':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[11,35,11,11,11,35,35,35,11,35,11,11,35,35,]),'linea':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'sentencia_while':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'sentencia_if':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'tipado':([5,6,9,27,28,34,36,41,42,56,58,59,61,81,122,123,133,134,],[15,32,15,51,52,15,32,15,15,15,15,15,15,15,15,15,15,15,]),'mensaje':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'modificadores':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'cabecera_while':([5,9,34,41,42,56,58,59,61,81,122,123,133,134,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'cabecera_if':([5,9,34,41,42,43,56,58,59,61,81,122,123,133,134,],[20,20,20,20,20,60,20,20,20,20,20,20,20,20,20,]),'assigment':([21,22,23,24,],[44,46,47,48,]),'expression_comparacion':([53,54,93,94,126,],[68,73,114,115,136,]),'double_expression_comparacion':([53,54,126,],[69,74,137,]),'numero_identificador':([53,54,93,94,96,97,98,99,100,101,126,],[70,70,70,70,116,117,118,119,120,121,70,]),'expression_cadena':([57,132,],[77,138,]),'expression':([62,63,64,65,84,108,109,110,111,147,],[83,86,87,88,112,127,128,129,130,150,]),'expression_caracter':([66,],[89,]),'cabecera_do_while':([79,],[105,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PUBLIC CLASS Identificador LlaveIzquierda instrucciones LlaveDerecha','program',6,'p_program','java_parser.py',21),
  ('instrucciones -> metodo_main LlaveIzquierda declaration_list LlaveDerecha','instrucciones',4,'p_instrucciones','java_parser.py',24),
  ('instrucciones -> declaration_list','instrucciones',1,'p_instrucciones','java_parser.py',25),
  ('metodo_main -> PUBLIC STATIC VOID MAIN ParentesisIzquierdo STRING CorcheteIzquierda CorcheteDerecha ARGS ParentesisDerecho','metodo_main',10,'p_metodo_main','java_parser.py',29),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','java_parser.py',33),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','java_parser.py',34),
  ('declaration -> linea','declaration',1,'p_declaration','java_parser.py',41),
  ('declaration -> sentencia_while','declaration',1,'p_declaration','java_parser.py',42),
  ('declaration -> sentencia_if','declaration',1,'p_declaration','java_parser.py',43),
  ('linea -> tipado PuntoyComa','linea',2,'p_linea','java_parser.py',48),
  ('linea -> mensaje PuntoyComa','linea',2,'p_linea','java_parser.py',49),
  ('linea -> modificadores PuntoyComa','linea',2,'p_linea','java_parser.py',50),
  ('modificadores -> PUBLIC tipado','modificadores',2,'p_modificadores','java_parser.py',54),
  ('modificadores -> PRIVATE tipado','modificadores',2,'p_modificadores','java_parser.py',55),
  ('modificadores -> PROTECTED tipado','modificadores',2,'p_modificadores','java_parser.py',56),
  ('tipado -> FLOAT assigment','tipado',2,'p_tipado','java_parser.py',59),
  ('tipado -> STRING Identificador Asignacion expression_cadena','tipado',4,'p_tipado','java_parser.py',60),
  ('tipado -> INT assigment','tipado',2,'p_tipado','java_parser.py',61),
  ('tipado -> DOUBLE assigment','tipado',2,'p_tipado','java_parser.py',62),
  ('tipado -> BOOLEAN assigment','tipado',2,'p_tipado','java_parser.py',63),
  ('tipado -> CHAR Identificador Asignacion expression_caracter','tipado',4,'p_tipado','java_parser.py',64),
  ('mensaje -> SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena ParentesisDerecho','mensaje',8,'p_mensaje','java_parser.py',69),
  ('mensaje -> SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo Identificador ParentesisDerecho','mensaje',8,'p_mensaje','java_parser.py',70),
  ('mensaje -> SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo expression_cadena SignoMas expression ParentesisDerecho','mensaje',10,'p_mensaje','java_parser.py',71),
  ('mensaje -> SYSTEM Punto OUT Punto PRINT ParentesisIzquierdo ParentesisDerecho','mensaje',7,'p_mensaje','java_parser.py',72),
  ('sentencia_while -> DO LlaveIzquierda declaration_list LlaveDerecha cabecera_do_while PuntoyComa','sentencia_while',6,'p_sentencia_while','java_parser.py',75),
  ('sentencia_while -> cabecera_while LlaveIzquierda declaration_list LlaveDerecha','sentencia_while',4,'p_sentencia_while','java_parser.py',76),
  ('sentencia_if -> cabecera_if ELSE LlaveIzquierda declaration_list LlaveDerecha','sentencia_if',5,'p_sentencia_if','java_parser.py',79),
  ('sentencia_if -> cabecera_if ELSE cabecera_if','sentencia_if',3,'p_sentencia_if','java_parser.py',80),
  ('sentencia_if -> cabecera_if','sentencia_if',1,'p_sentencia_if','java_parser.py',81),
  ('cabecera_do_while -> WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho','cabecera_do_while',4,'p_cabecera_do_while','java_parser.py',84),
  ('cabecera_do_while -> WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerecho','cabecera_do_while',4,'p_cabecera_do_while','java_parser.py',85),
  ('cabecera_while -> WHILE ParentesisIzquierdo expression_comparacion ParentesisDerecho','cabecera_while',4,'p_cabecera_while','java_parser.py',88),
  ('cabecera_while -> WHILE ParentesisIzquierdo double_expression_comparacion ParentesisDerecho','cabecera_while',4,'p_cabecera_while','java_parser.py',89),
  ('cabecera_if -> IF ParentesisIzquierdo expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerecha','cabecera_if',7,'p_cabecera_if','java_parser.py',93),
  ('cabecera_if -> IF ParentesisIzquierdo double_expression_comparacion ParentesisDerecho LlaveIzquierda declaration_list LlaveDerecha','cabecera_if',7,'p_cabecera_if','java_parser.py',94),
  ('assigment -> Identificador Asignacion expression','assigment',3,'p_assignment','java_parser.py',97),
  ('assigment -> Identificador MasIgual expression','assigment',3,'p_assignment','java_parser.py',98),
  ('assigment -> Identificador MenosIgual expression','assigment',3,'p_assignment','java_parser.py',99),
  ('assigment -> Identificador DivisionIgual expression','assigment',3,'p_assignment','java_parser.py',100),
  ('assigment -> Identificador','assigment',1,'p_assignment','java_parser.py',101),
  ('expression_cadena -> CADENADECARACTERES','expression_cadena',1,'p_expression_cadena','java_parser.py',104),
  ('expression_caracter -> CARACTER','expression_caracter',1,'p_expression_caracter','java_parser.py',107),
  ('empty -> <empty>','empty',0,'p_empty','java_parser.py',111),
  ('double_expression_comparacion -> expression_comparacion OR expression_comparacion','double_expression_comparacion',3,'p_double_expression_comparacion','java_parser.py',114),
  ('double_expression_comparacion -> expression_comparacion AND expression_comparacion','double_expression_comparacion',3,'p_double_expression_comparacion','java_parser.py',115),
  ('numero_identificador -> Numero','numero_identificador',1,'p_numero_identificador','java_parser.py',118),
  ('numero_identificador -> Identificador','numero_identificador',1,'p_numero_identificador','java_parser.py',119),
  ('expression_comparacion -> numero_identificador Diferente numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',123),
  ('expression_comparacion -> numero_identificador Mayor numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',124),
  ('expression_comparacion -> numero_identificador MayorIgual numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',125),
  ('expression_comparacion -> numero_identificador Menor numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',126),
  ('expression_comparacion -> numero_identificador MenorIgual numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',127),
  ('expression_comparacion -> numero_identificador ComparacionIgual numero_identificador','expression_comparacion',3,'p_expression_comparacion','java_parser.py',128),
  ('expression -> expression SignoMas expression','expression',3,'p_expression','java_parser.py',131),
  ('expression -> expression SignoMenos expression','expression',3,'p_expression','java_parser.py',132),
  ('expression -> expression SignoMultiplicar expression','expression',3,'p_expression','java_parser.py',133),
  ('expression -> expression SignoDividir expression','expression',3,'p_expression','java_parser.py',134),
  ('expression -> ParentesisIzquierdo expression ParentesisDerecho','expression',3,'p_expression','java_parser.py',135),
  ('expression -> Numero','expression',1,'p_expression','java_parser.py',136),
  ('expression -> Identificador','expression',1,'p_expression','java_parser.py',137),
]