# =================================================================================
# Parser for one instruction only
# =================================================================================
import yacc
import lexer

tokens = lexer.tokens  # token list

# Lists use and kill are used in livenessAnalysis.py for the algorithm
use = []
kill = []

def p_instruction_assign_array(p):
    '''instruction  : VARIABLE ARRAY E ARRAY ASSIGN E'''
    kill.append(p[1])

def p_instruction_assign_array_toArray(p):
    '''instruction  : VARIABLE ARRAY E ARRAY ASSIGN E_ARRAY'''
    kill.append(p[1])

def p_instruction_assign(p):
    '''instruction  : VARIABLE ASSIGN E'''
    kill.append(p[1])

def p_instruction_e_array(p):
    '''instruction  : VARIABLE ASSIGN E_ARRAY'''
    kill.append(p[1])

def p_instruction_if_variables(p):
    '''instruction  : IFFALSE VARIABLE LGT VARIABLE GOTO NUMBER
                    | IF VARIABLE LGT VARIABLE GOTO NUMBER '''
    use.append(p[2])
    use.append(p[4])

def p_instruction_if_varnum(p):
    '''instruction  : IFFALSE VARIABLE LGT NUMBER GOTO NUMBER
                    | IF VARIABLE LGT NUMBER GOTO NUMBER'''
    use.append(p[2])

def p_instruction_if_numvar(p):
    '''instruction  : IFFALSE NUMBER LGT VARIABLE GOTO NUMBER
                    | IF NUMBER LGT VARIABLE GOTO NUMBER  '''
    use.append(p[4])

def p_instruction_if_num(p):
    '''instruction  : IFFALSE NUMBER LGT NUMBER GOTO NUMBER
                    | IF NUMBER LGT NUMBER GOTO NUMBER'''

def p_instruction_return_variable(p):
    '''instruction  : RETURN VARIABLE '''
    use.append(p[2])

def p_instruction_return_number(p):
    '''instruction  : RETURN NUMBER '''

def p_E_array(p):
    '''E_ARRAY : VARIABLE ARRAY E ARRAY '''
    use.append(p[1])

def p_E_operator(p):
    '''E : E OPERATOR E '''

def p_E_number(p):
    '''E : NUMBER '''

def p_E_variable(p):
    '''E : VARIABLE '''
    use.append(p[1])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

yacc.yacc()

def main():
    data = """ return 5 """
    yacc.parse(data)
    print(use, kill)

if __name__ == "__main__":
    main()
