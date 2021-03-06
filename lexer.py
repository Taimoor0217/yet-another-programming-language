import ply.lex as lex

t_ignore                = ' \t\v\r' # whitespace

t_EQEQ = r'=='
t_DOT = r'\.'
t_EQUAL = r'='
t_LCURL = r'\{'
t_RCURL = r'\}'
t_DIVIDE =  r'/'
t_LPAREN =   r'\('
t_RPAREN =   r'\)'
t_SUB = r'-'
t_MULTIPLY = r'\*'
t_POWER = r'\^'
t_ADD = r'\+'
t_MOD = r'\%'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_GREATER = r'\>'
t_LESSER = r'\<'
t_LEEQ = r'<='
t_GEEQ = r'>='
t_NOEQ = r'!='


tokens = (
        'COMMA','EQUAL', 'TYPE','SEMICOLON', 'COLON',
        'STRING','CHAR','INT', 'DOUBLE','BOOL','VARNAME' ,
        'ADD','SUB','DIVIDE','MULTIPLY','MOD','PLUSPLUS','MINUSMINUS',
        'LPAREN','RPAREN','LCURL','RCURL', 'STRUCT', 'INJECT',
        'GREATER','LESSER','LEEQ','GEEQ','NOEQ','EQEQ', 'DOT',
        'FOR', 'PRINT', 'NOT' , 'AND', 'OR' , 'FALSE' , 'TRUE', 'POWER'
)

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1
        pass


def t_error(T):
	pass

def t_TYPE(t):
        r'INT|DOUBLE|BOOL|CHAR|STRING'
        return t

def t_NOT(t):
        r'NOT'
        return t
def t_FALSE(t):
        r'FALSE'
        return t
def t_TRUE(t):
        r'TRUE'
        return t
def t_AND(t):
        r'AND'
        return t

def t_OR(t):
        r'OR'
        return t

def t_FOR(t):
        r'FOR'
        return t

def t_INJECT(t):
        r'<-'
        return t

def t_PRINT(t):
        r'PRINT'
        return t

def t_STRING(t):
        r'"[^"]*"'
        t.value = t.value[1:-1] # drop "surrounding quotes"
        return t

def t_DOUBLE(t):
        r'\d*\.\d+'
        t.value=float(t.value)
        return t

def t_STRUCT(t):
        r'STRUCT'
        return t 

def t_INT(t):
        r'\d+'
        t.value=int(t.value)
        return t

def t_COMMA(t):
        r','
        return t 


def t_SEMICOLON(t):
        r';'
        return t
def t_COLON(t):
        r':'
        return t
def t_CHAR(t):
        r'(L)?\'([^\\\n]|(\\.))*?\''
        return t
def t_BOOL(t):
        r'TRUE|FALSE'
        return t 
def t_VARNAME(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return t

# text = """STRUCT N{
#     PRINT("HELLO WORLD")
# }"""

# lex.lex()
# lex.input(text)
# while True:
#         tok = lex.token()
#         if not tok: break
#         print (tok)