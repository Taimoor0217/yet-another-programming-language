import lexer
import ply.lex as lex
import ply.yacc as yacc

start = 'exp'

precedence = (
        ('left', 'EQEQ'),
        ('left', 'LESSER', 'LEEQ', 'GREATER', 'GEEQ'),
        ('left', 'ADD', 'SUB' , 'POWER'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('right', 'NOEQ'),
)

tokens = (
        'COMMA','EQUAL', 'TYPE','SEMICOLON', 'COLON',
        'STRING','CHAR','INT', 'DOUBLE','BOOL','VARNAME' ,
        'ADD','SUB','DIVIDE','MULTIPLY','MOD','PLUSPLUS','MINUSMINUS',
        'LPAREN','RPAREN','LCURL','RCURL', 'POWER', 'INJECT',
        'GREATER','LESSER','LEEQ','GEEQ','NOEQ','EQEQ','STRUCT',
        'FOR','PRINT', 'TO' , 'NOT' , 'AND' , 'OR' , 'FALSE' , 'TRUE' , 'DOT'
)

def p_exp_stmnts(p): #statment followed by statements
	'stmnts : stmnt stmnts'
	p[0] = [p[1]] + p[2]

def p_exp_print (p): #tuples for print statement
    'exp : exp COMMA exp'
    p[0] = ("print tuple" , p[1] , p[3])

def p_exp_stempty(p): #empty statement
	'stmnts : '
	p[0] = []

def p_exp_bool(p):
	"""exp : FALSE 
        | TRUE """
	p[0] = ('bool' , p[1])

# def p_exp_true(p):
# 	'exp : TRUE'
# 	p[0] = ('bool' , p[1])

def p_stmnt_start(p):
	'exp : stmnts'
	p[0] = p[1]

def p_stmnt_inn(p): #increment by 1
	"""stmnt : VARNAME PLUSPLUS SEMICOLON
    | VARNAME PLUSPLUS """
	p[0] = ("plusplus", p[1])

def p_stmnt_dnn(p): #decrement by 1
	"""stmnt : VARNAME MINUSMINUS SEMICOLON
    | VARNAME MINUSMINUS"""
	p[0] = ("minusminus", p[1])



def p_stmnt_declaration(p): #declaration of a variable with value
	"""stmnt : TYPE VARNAME vnames EQUAL exp
        | TYPE VARNAME vnames EQUAL exp SEMICOLON """
	p[0] = ("identifier", p[1], [p[2]]+p[3], p[5])

def p_stmnt_valueless(p): #variable declaration without value
	'stmnt : TYPE VARNAME vnames SEMICOLON'
	p[0] = ("declaration", p[1], p[2])

def p_stmnt_assignment(p): #declaration of a variable with value
	'stmnt : VARNAME EQUAL exp SEMICOLON'
	p[0] = ("assignment", p[1], p[3])


def p_stmnt_for(p): #for loop with its variables
	"""stmnt : FOR LPAREN exp COLON exp COLON exp RPAREN LCURL stmnts RCURL"""
	p[0] = ("FOR", p[3][0] , p[5] , p[7][0] , p[10] )


def p_stmnt_print(p): #print statement
	'stmnt : PRINT LPAREN exp RPAREN SEMICOLON'
	p[0] = ("print", [p[3]] )

def p_closed_exp(p): #closed expression
	'exp : LPAREN exp RPAREN'
	p[0] = ("closed_expression", p[2] )

def p_ch_ch(p):
	"""choice : PLUSPLUS
		| MINUSMINUS"""
	p[0] = p[1]

def p_attr_attr(p):
	'attrs : TYPE VARNAME attrs2'
	p[0] = [("attr",p[1],  p[2])] +p[3]

def p_attr_attrs2(p):
	"""attrs2 : COMMA attrs
		| """
	if len(p)>1:
		p[0] = p[2]
	else:
		p[0] = []

def p_exp_emp(p):
	'exp : '
	p[0] = []

def p_vnames_emo(p):
	'vnames : COMMA VARNAME vnames'
	p[0] = [p[2]] + p[3]

def p_vnames_empty(p):
	'vnames : '
	p[0] = []

def p_value_int(p):
	'exp : INT'
	p[0] = ("int", p[1])
def p_value_char(p):
	'exp : CHAR'
	p[0] = ("char", p[1])
def p_value_string(p):
	'exp : STRING'
	p[0] = ("string", p[1])
def p_value_double(p):
	'exp : DOUBLE'
	p[0] = ("double", p[1])
def p_value_bool(p):
	'exp : BOOL'
	p[0] = ("bool", p[1])

def p_value_vname(p):
	'exp : VARNAME '
	p[0] = ("vname", p[1])


def p_exp_binaryop(p):
	"""exp : exp ADD exp 
		| exp SUB exp 
		| exp MULTIPLY exp 
		| exp POWER exp 
		| exp DIVIDE exp 
		| exp MOD exp"""
	p[0] = ("binary operation", p[1], p[2], p[3])

def p_exp_compareop(p):
	"""exp : exp EQEQ exp 
		| exp LEEQ exp 
		| exp GEEQ exp 
		| exp GREATER exp 
		| exp LESSER exp
		| exp NOEQ exp"""
	p[0] = ("comparison operation", p[1], p[2], p[3])

def p_exp_logop(p):
	"""exp : exp OR exp 
		| exp AND exp 
		| exp NOT exp"""
	p[0] = ("logical operation", p[1], p[2], p[3])
    
def p_exp_crement(p):
	"""exp : exp PLUSPLUS  
		| exp MINUSMINUS"""
	p[0] = ("crement", p[1], p[2])

def p_stmnt_struct_declaration(p):#declaration of a struct
	'stmnt : STRUCT VARNAME LCURL stmnts RCURL SEMICOLON'
	p[0] = ("struct declaration", p[2], p[4] )	

def p_struct_instance(p):
	'stmnt : VARNAME VARNAME SEMICOLON'
	p[0] = ("struct instance" , p[1] , p[2] )

def p_struct_reference(p):
	'exp : VARNAME DOT VARNAME'
	p[0] = ("struct reference" , p[1] , p[3])

def p_struct_attr_assignment(p):
	'stmnt : VARNAME DOT VARNAME INJECT exp SEMICOLON'
	p[0] = ("struct attr assignment", p[1] , p[3] , p[5])

def p_error(p):
	print ("Check syntax in line: " , p)

# jslexer = lex.lex(module=lexer)
# jsparser = yacc.yacc()
# jsast = jsparser.parse(""" INT X = 1;""",lexer=jslexer)
# print (jsast)
