import yacc as yacc
import lexer

tokens = lexer.tokens  # token list

def p_instruction(p):
    '''instruction : VARIABLE ASSIGN expression'''

def p_expression(p):
    '''expression  : NUMBER
                   | VARIABLE'''

yacc.yacc()

data = """ t1 := b * d """
yacc.parse(data)
