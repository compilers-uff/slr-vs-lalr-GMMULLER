import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = [
    'EQUAL',
    'STAR',
    'ID'
]

def t_EQUAL(t):
    r'='
    t.value = 'EQUAL'
    return t

def t_STAR(t):
    r'\*' 
    t.value = 'STAR'
    return t

def t_ID(t): 
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_1(p):
    'S : L EQUAL R'

def p_2(p):
    'S : R'

def p_3(p):
    'L : STAR R'

def p_4(p):
    'L : ID'

def p_5(p):
    'R : L'

def p_error(p):
    print("Syntax error at '%s'" % p.value)

if __name__ == '__main__':
    lex.lex()
    yacc.yacc(method='SLR', debug=True)
    # yacc.yacc(method='LALR', debug=True) # Basta alternar o parametro metodo para escolher outro tipo de parser
    