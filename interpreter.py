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

def Identifier(env , tree):
    #this does not handle updating the value of a variable i-e X = 10
    # print(tree)
    Type = tree[1]
    variable = tree[2][0]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        value = eval_expression(env , tree[3])
        if Type == tree[3][0].upper() or ( Type == "INT" and tree[3][0] == "binary operation"  ): # assuming there will only be statements like INT A = 10; and not like INT A = 10 + 10;
            set_variable(env , Type, variable , value)
        else:
            Error("Type mismatch for variable {}, cannot assign {} to {}".format(variable , tree[3][0].upper() , Type))
    else:
        Error("Redeclaration of Variable {} \n Already declared with value: {}".format(variable , val) )
    return variable
def Binop(env, tree):
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    if type(LHS) != type(RHS):
        Error("Type mismatch for {} {} {}".format(type(LHS) , operation , type(RHS)))

    if operation == '+':
        return LHS + RHS
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

def Compop(env , tree): #comparison operations
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    if type(LHS) != type(RHS):
        Error("Cannot compare {} with {}".format(type(LHS) , type(RHS)))
    
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
    Val = get_variable(env , tree[1][0])
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
    #copy dictionary to the new envoirnment
    decl = tree[1]
    dump = []
    condition = tree[2]
    change = tree[3]
    statements = tree[4]
    dump.append(eval_expression(env , decl))
    while eval_expression(env , condition):
        for s in statements:
            eval_expression(env , s)
        eval_expression(env , change)

    for d in dump:
        del env["variables"][d]
        # set_variable(env ,"" , d , sys.maxsize )
def eval_expression(env , tree):
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
        return Identifier(env , tree)
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


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.read()

    jslexer = lex.lex(module=lexer)
    jsparser = yacc.yacc(module=parser)
    jsast = jsparser.parse(data)
    # print(jsast)
    ENV = {
        "variables": {},
        "Temps": {}
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
