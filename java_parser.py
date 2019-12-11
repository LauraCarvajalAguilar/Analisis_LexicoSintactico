import sys
import ply.yacc as yacc
from java_lexer import tokens
VERBOSE = 1
precedence = (
	('left', 'IMPLEMENTS', 'IMPORT'),
	('left', 'COMA'),
    ('left', 'Asignacion', 'MasIgual', 'MenosIgual', 'MultiplicacionIgual', 'DivisionIgual'),
	('left', 'PuntoyComa'),
	('left', 'OR'),
	('left', 'AND'),
	('nonassoc', 'ComparacionIgual', 'Diferente'),
    ('nonassoc', 'SignoMenos', 'MenorIgual', 'Mayor', 'MayorIgual'),
	('left', 'SignoMas', 'SignoMenos'),
    ('left', 'ELSE'),
	('right', 'CorcheteIzquierda'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'FINAL'),
)

def p_program(p):
    'program : PUBLIC CLASS Identificador LlaveIzquierda instrucciones  LlaveDerecha'
	
def p_instrucciones(p):
	'''instrucciones : metodo_main LlaveIzquierda declaration_list LlaveDerecha
					 | declaration_list
					 '''
	pass
def p_metodo_main(p):
	'''metodo_main : PUBLIC STATIC VOID MAIN ParentesisIzquierdo STRING CorcheteIzquierda CorcheteDerecha ARGS ParentesisDerecho
					'''
	pass
def p_declaration_list(p):
   '''declaration_list : declaration_list  declaration
   					   | declaration 
					   
					   
   '''
   pass

def p_declaration(p):
	'''declaration : linea
				   | sentencia_while
				   | sentencia_if'''
	pass
