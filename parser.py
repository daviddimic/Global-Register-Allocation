# =================================================================================
# Parser for one instruction only
# =================================================================================
import yacc as yacc
import lexer

tokens = lexer.tokens  # token list
use = []
kill = []

def p_instruction_assign_num(p):
    '''instruction  : VARIABLE ASSIGN NUMBER '''
    kill.append(p[1])

def p_instruction_assign_var(p):
    '''instruction  : VARIABLE ASSIGN VARIABLE '''
    use.append(p[3])
    kill.append(p[1])

def p_instruction_assign_variables(p):
    '''instruction  : VARIABLE OPERATOR VARIABLE'''
    use.append(p[1])
    use.append(p[3])

def p_instruction_assign_varnum(p):
    '''instruction  : VARIABLE OPERATOR NUMBER'''
    use.append(p[1])

def p_instruction_assign_numvar(p):
    '''instruction  : NUMBER OPERATOR VARIABLE'''
    use.append(p[3])

def p_instruction_assign_numbers(p):
    '''instruction  : NUMBER OPERATOR NUMBER'''

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

def p_instruction_return(p):
    '''instruction  : RETURN VARIABLE '''
    use.append(p[2])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

yacc.yacc()

def main():
    data = """ t := a """
    yacc.parse(data)
    print(use)

if __name__ == "__main__":
    main()
