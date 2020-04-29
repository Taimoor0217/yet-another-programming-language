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
    return env["variables"].get(v , sys.maxsize)

def set_variable(env , Type , v , value):
    env["variables"][v] = (Type , value)
    return value

def Error(e):
   print(f"{bcolors.FAIL} {e}")
   raise SystemExit

def Identifier(env , tree):
    #this does not handle updating the value of a variable i-e X = 10
    print(tree)
    Type = tree[1]
    variable = tree[2][0]
    val = get_variable(env , variable)
    if val == sys.maxsize:
        if Type == tree[3][0].upper(): # assuming there will only be statements like INT A = 10; and not like INT A = 10 + 10;
            value = eval_expression(env , tree[3])
            set_variable(env , Type, variable , value)
        else:
            Error("Type mismatch for variable {}, cannot assign {} to {}".format(variable , tree[3][0].upper() , Type))
    else:
        Error("Redeclaration of Variable {} \n Already declared with value: {}".format(variable , val) )

def Binop(env, tree):
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    if LHS == "?/?/" or RHS == "?/?/":
        Error("Undeclared Variables !")

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

def Compop(env , tree):
    operation = tree[2]
    LHS = eval_expression(env , tree[1])
    RHS = eval_expression(env , tree[3])

    if LHS == "?/?/" or RHS == "?/?/":
        Error("Undeclared Variables !")

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

def Logop(env , tree):
    operation = tree[2]
    RHS = eval_expression(env , tree[3])
    if RHS == "?/?/":
        Error("Undeclared Variables !")

    if operation == "NOT":
        return not (RHS != False)

    LHS = eval_expression(env , tree[1])

    if LHS == "?/?/":
        Error("Undeclared Variables !")

    if operation == "OR":
        return LHS != False or RHS != False
    if operation == "AND":
        return LHS != False and RHS != False

def Vname(env, tree):
    Val = get_variable(env , tree[1][0])
    if Val == sys.maxsize:
        return "?/?/"
    else:
        return Val[1]

def Pprint(env , tree):
    print(tree)
    print(eval_expression(env , tree[1][0])) #recursively evaluate and print the elements

def Tprint(env , tree, ans): #incase there are tuples in print
    for t in tree[1:]:
        ans += " " +str(eval_expression(env , t))
    return ans[1:]



def eval_expression(env , tree):
    node_type = tree[0] 
    #base cases
    if node_type == "int":
        return int(tree[1])
    if node_type == "double":
        return float(tree[1])
    if node_type == "bool":
        return tree[1]
    if node_type == "string":
        return tree[1]
    if node_type == "char":
        return tree[1]
    if node_type == "false":
        return False
    if node_type == "true":
        return True
    if node_type == "identifier":
        return Identifier(env , tree)
    if node_type == "binary operation":
        return Binop(env , tree)
    if node_type == "comparison operation":
        return Compop(env , tree )
    if node_type == "logical operation":
        return Logop(env , tree )

    if node_type == "vname":
        return Vname(env , tree)
    if node_type == "print":
        return Pprint(env , tree)
    if node_type == "print tuple":
        return Tprint(env , tree , '') 
    


def main():
    with open('testcases.txt', 'r') as f:
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
            # print(ENV)
    

if __name__ == "__main__":
    main()
