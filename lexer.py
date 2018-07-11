import lex

tokens = (
    'NUMBER',
    'VARIABLE',
    'OPERATOR',
    'LGT',
    'ASSIGN',
    'IF',
    'GOTO',
    'IFFALSE',
    'RETURN',
    'ARRAY'
)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IFFALSE(t):
    r'(ifFalse)|(IFFALSE)|(iffalse)'
    t.value = "ifFalse"
    return t

def t_IF(t):
    r'(if)|(IF)'
    t.value = t.value.lower()
    return t

def t_ARRAY(t):
    r'[\[\]]'
    return t

def t_GOTO(t):
    r'(goto)|(GOTO)'
    t.value = t.value.lower()
    return t

def t_RETURN(t):
    r'(return)|(RETURN)'
    t.value = t.value.lower()
    return t

def t_VARIABLE(t):
    r'[A-Za-z]+[0-9]?'
    return t

def t_OPERATOR(t):
    r'[+*/-]'
    return t

def t_LGT(t):
    r'(<=)|[<>]|(>=)'
    return t

def t_ASSIGN(t):
    r':='
    return t

t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character: %s" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# data = """ IFFALSE t < 3 GOTO 3 """
#
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
