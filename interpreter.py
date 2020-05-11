import lexer
import parser
import ply.lex as lex
import ply.yacc as yacc
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_variable(env , v):
    return env["variables"].get(v , sys.maxsize) # return maxsize if variable not found

def set_variable(env , Type , v , value):
    env["variables"][v] = (type(value) , value)
    return value

def Error(e):
   print(f"{bcolors.FAIL} {e}")
   raise SystemExit

def Identifier(env , tree, dump):
    #this does not handle updating the value of a variable i-e X = 10
    # print(tree)
    Type = tree[1]
    variable = tree[2][0]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        value = eval_expression(env , tree[3])
        # if Type == tree[3][0].upper() or ( Type == "INT" and tree[3][0] == "binary operation"  ): # assuming there will only be statements like INT A = 10; and not like INT A = 10 + 10;
        set_variable(env , Type, variable , value)
        if dump is not None: #push the variable to the dump from where it can be removed after its scope
            dump += [variable]
        # else:
        #     Error("Type mismatch for variable {}, cannot assign {} to {}".format(variable , tree[3][0].upper() , Type))
    else:
        Error("Redeclaration of Variable {} \n Already declared with value: {}".format(variable , val) )
    return variable
def Binop(env, tree):
    #doesnot support -b or -X
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    # if type(LHS) != type(RHS):
    #     Error("Type mismatch for {} {} {}".format(type(LHS) , operation , type(RHS)))
    try:
        if operation == '+':
            return LHS + RHS
        if operation == '^':
            return LHS**RHS
        if operation == '-':
            return LHS - RHS
        if operation == '*':
            return LHS * RHS
        if operation == '/':
            if RHS == 0:
                Error("Division by Zero")
            return LHS / RHS
        if operation == '%':
            return LHS % RHS
    except TypeError:
        Error("TypeError: Cannot perform {} on {} and {}".format(operation , type(LHS), type(RHS)))

def Compop(env , tree): #comparison operations
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    # if type(LHS) != type(RHS):
    #     Error("Cannot compare {} with {}".format(type(LHS) , type(RHS)))
    
    if operation == "==":
        return LHS == RHS
    if operation == ">=":
        return LHS>=RHS
    if operation == "<=":
        return LHS <= RHS
    if operation == "!=":
        return LHS != RHS
    if operation == ">":
        return LHS > RHS
    if operation == "<":
        return LHS < RHS

def Logop(env , tree): #logical operation
    operation = tree[2]
    RHS = eval_expression(env , tree[3])
    if operation == "NOT":
        return not (RHS != False)

    LHS = eval_expression(env , tree[1])
    if operation == "OR":
        return LHS != False or RHS != False
    if operation == "AND":
        return LHS != False and RHS != False

def Vname(env, tree):
    # print(tree)
    Val = get_variable(env , tree[1])
    if Val == sys.maxsize or Val == -sys.maxsize:
        Error("Undeclared Variable {}".format(tree[1][0]))
    else:
        return Val[1]

def Pprint(env , tree):
    # print(tree)
    print(eval_expression(env , tree[1][0])) #recursively evaluate and print the elements

def Tprint(env , tree, ans): #incase there are tuples in print
    for t in tree[1:]:
        ans += " " +str(eval_expression(env , t))
    return ans[1:]

def Declaration(env , tree):
    Type = tree[1]
    variable = tree[2][0]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        if Type == "INT":
            set_variable(env , Type, variable , -sys.maxsize)
        else:
            set_variable(env , Type, variable , str(-sys.maxsize) )
    else:
        Error("Redeclaration of Variable {} \n Already declared with value: {}".format(variable , val) )

def Assignment(env , tree):
    # Type =
    variable = tree[1]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        Error("Undeclared Variables !")
    RHS = eval_expression(env , tree[2])
    if type(RHS) == val[0]:
        set_variable(env , type(RHS) , variable , RHS)
    else:
        Error("Type Mismatch")
        
def Increment(env , tree , Type):
    variable = tree[1]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        Error("Undeclared Variable {}!".format(variable))
    if Type == "pp": 
        set_variable(env , "" , variable , val[1]+1)
    else:
        set_variable(env , "" , variable , val[1]-1)

def For_Loop(env , tree):
    decl = tree[1]
    dump = []
    condition = tree[2]
    change = tree[3]
    statements = tree[4]
    eval_expression(env , decl , dump=dump)
    while eval_expression(env , condition):
        for s in statements:
            eval_expression(env , s , dump=dump)
        eval_expression(env , change)

    for d in dump: #dump the variables in this scope
        del env["variables"][d]
        # set_variable(env ,"" , d , sys.maxsize )
def closed_exp(env , tree):
    # print(tree)
    return eval_expression(env , tree[1])

def struct_declaration(env , tree):
    def check_red(Vars ,  v):
        for N in Vars:
            if N[1] == v:
                return False
        return True
    name = tree[1]
    variables = tree[2]
    N_VARS = []
    if env["structs"].get(name , sys.maxsize) == sys.maxsize:
        for v in variables:
            if v[0] == "declaration":
                if check_red(N_VARS , v[2]):
                    N_VARS.append(v[1:])
                else:
                    Error("Redeclaration of varaiable {} in declaraton of STRUCT {}".format(v[2] , name))
            else:
                Error("Syntax error in the declaration of STRUCT {}".format(name))
        env["structs"][name] = {
            "Vars": N_VARS
        }
    else:
        Error("Redeclration of already defined struct")

def struct_instance(env , tree):
    def build_instance(s_type):
        ins = {}
        for i in s_type["Vars"]:
            ins[i] = None #How about sys.max size?
        return ins
    _type = tree[1]
    s_type = env["structs"].get(_type , None)
    if s_type is None:
        Error("Undefined Type: {} ".format(_type))
    else:
        instance = build_instance(s_type)
        Name = tree[2]
        env["instances"][Name] = instance
    print(env)
    
def eval_expression(env , tree , *args, **kwargs):
    if len(tree) < 1:
        return 0
        
    node_type = tree[0] 
    #base cases
    if node_type == "int":
        return int(tree[1])
    if node_type == "double":
        return float(tree[1])
    if node_type == "string":
        return tree[1]
    if node_type == "char":
        return tree[1]
    if node_type == "bool":
        return not tree[1] == "FALSE"
    if node_type == "identifier":
        return Identifier(env , tree , dump=kwargs.get('dump', None))
    if node_type == "binary operation":
        return Binop(env , tree)
    if node_type == "comparison operation":
        return Compop(env , tree )
    if node_type == "logical operation":
        return Logop(env , tree )
    if node_type == "declaration":
        return Declaration(env , tree)
    if node_type == "assignment":
        return Assignment(env , tree)
    if node_type == "vname":
        return Vname(env , tree)
    if node_type == "print":
        return Pprint(env , tree)
    if node_type == "print tuple":
        return Tprint(env , tree , '')
    if node_type == "plusplus":
        return Increment(env , tree , "pp")
    if node_type == "minusminus":
        return Increment(env , tree , "mm")
    if node_type == "FOR":
        return For_Loop(env , tree)
    if node_type == "closed_expression":
        return closed_exp(env , tree)
    if node_type == "struct declaration":
        return struct_declaration(env , tree)
    if node_type == "struct instance":
        return struct_instance(env , tree)


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.read()

    jslexer = lex.lex(module=lexer)
    jsparser = yacc.yacc(module=parser)
    jsast = jsparser.parse(data)
    # print(jsast)
    ENV = {
        "variables": {},
        "structs": {},
        "instances": {}
    }
    # LOOP_ENV = {}
    if len(jsast) == 1:
        eval_expression(ENV , jsast[0])
    else:
        for v in jsast:
            eval_expression(ENV , v)
            # print(ENV["variables"])
    

if __name__ == "__main__":
    main()
