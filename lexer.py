# lexer.py

import ply.lex as lex

# Lista de tokens
tokens = (
    'INCLUDE',      # Directiva #include
    'HEADER',       # Archivo de encabezado entre <>
    'NUMBER',       # Número entero
    'ID',           # Identificador
    'EQUALS',       # Signo de igual '='
    'SEMICOLON',    # Punto y coma ';'
    'PLUS',         # Signo más '+'
    'LPAREN',       # Paréntesis izquierdo '('
    'RPAREN',       # Paréntesis derecho ')'
    'LBRACE',       # Llave izquierda '{'
    'RBRACE',       # Llave derecha '}'
    'COMMA',        # Coma ','
    'RETURN',       # Palabra clave return
    'FOR',          # Palabra clave for
    'INT',          # Palabra clave int
    'MULT',
    'EQUALS_EQUALS',
    'LEQ',          # Operador menor o igual '<='
    'INCREMENT'     # Operador de incremento '++'
)

t_EQUALS = r'='
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_MULT = r'\*'
t_EQUALS_EQUALS = r'=='
t_LEQ = r'<='
t_INCREMENT = r'\+\+'

def t_INCLUDE(t):
    r'\#include'
    return t

def t_HEADER(t):
    r'<[a-zA-Z_\.]+>'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_INT(t):
    r'int'
    return t

def t_FOR(t):
    r'for'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)
        
# Ignorar caracteres como espacios y saltos de línea
t_ignore = '\t'


# Manejo de errores léxicos
def t_error(t):
    print("Ilegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


# instanciamos el analizador lexico
lexer = lex.lex()

def tokenize(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value, tok.lineno, tok.lexpos))
    return tokens