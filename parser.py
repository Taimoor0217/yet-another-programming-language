import lexer
import ply.lex as lex
import ply.yacc as yacc

start = 'exp'

precedence = (
        ('left', 'EQEQ'),
        ('left', 'LESSER', 'LEEQ', 'GREATER', 'GEEQ'),
        ('left', 'ADD', 'SUB'),
        ('left', 'MULTIPLY', 'DIVIDE'),
        ('right', 'NOEQ'),
)

tokens = (
        'COMMA','EQUAL', 'TYPE','SEMICOLON', 'COLON',
        'STRING','CHAR','INT', 'DOUBLE','BOOL','VARNAME' ,
        'ADD','SUB','DIVIDE','MULTIPLY','MOD','PLUSPLUS','MINUSMINUS',
        'LPAREN','RPAREN','LCURL','RCURL',
        'GREATER','LESSER','LEEQ','GEEQ','NOEQ','EQEQ',
        'FOR','PRINT', 'TO'
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

def p_stmnt_start(p):
	'exp : stmnts'
	p[0] = p[1]

def p_stmnt_inn(p): #increment by 1
	'stmnt : VARNAME PLUSPLUS SEMICOLON'
	p[0] = ("plusplus", p[1])

def p_stmnt_dnn(p): #decrement by 1
	'stmnt : VARNAME MINUSMINUS SEMICOLON'
	p[0] = ("minusminus", p[1])



def p_stmnt_declaration(p): #declaration of a variable with value
	'stmnt : TYPE VARNAME vnames EQUAL exp SEMICOLON'
	p[0] = ("identifier", p[1], [p[2]]+p[3], p[5])

def p_stmnt_valueless(p): #variable declaration without value
	'stmnt : TYPE VARNAME vnames SEMICOLON'
	p[0] = ("declaration", p[1], [p[2]] + p[3])


def p_stmnt_for(p): #for loop with its variables
	'stmnt : FOR VARNAME INT TO INT choice LCURL stmnts RCURL'
	p[0] = ("FOR", p[2], p[3], p[5], p[6], p[8])


def p_stmnt_print(p): #print statement
	'stmnt : PRINT LPAREN exp RPAREN SEMICOLON'
	p[0] = ("print", [p[3]] )

    

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


# def p_stmnt_do(p):
# 	'stmnt : DO LCURL stmnts RCURL UNTIL LPAREN exp RPAREN'
# 	p[0] = ("dountil", p[3], p[7])

# def p_stmn_objf(p):
# 	'stmnt : OBJ VARNAME LCURL stmnts RCURL'
# 	p[0] = ("new obj", p[2], p[4])

# def p_stmnt_objc(p):
# 	'stmnt : OBJ VARNAME VARNAME SEMICOLON'
# 	p[0] = ("obj call", p[2], p[3])

# def p_exp_objexp(p):
# 	'stmnt : VARNAME DOT VARNAME EQUAL exp SEMICOLON'
# 	p[0] = ("objval",p[1],p[3],p[5])

# def p_exp_objone(p):
# 	'exp : VARNAME DOT VARNAME'
# 	p[0] = ("objret", p[1], p[3])

# def p_exp_arr(p):
# 	'exp : exp COMMA exp'
# 	p[0] = p[1] + p[3]

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


def p_exp_crement(p):
	"""exp : exp PLUSPLUS  
		| exp MINUSMINUS"""
	p[0] = ("crement", p[1], p[2])


def p_error(p):
	print ("Check syntax in line: " , p)

# jslexer = lex.lex(module=lexer)
# jsparser = yacc.yacc()
# jsast = jsparser.parse("""FOR I 3 to 5 ++ {
#     FOR J 3 to 10 ++{
#         PRINT( X+2 , 2+2 , 2+2  );
#     }
# }""",lexer=jslexer)
# print (jsast)
