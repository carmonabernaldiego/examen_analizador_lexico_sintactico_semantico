# parser.py

import ply.yacc as yacc
from lexer import tokens

# errores
errores = []

# Tabla de símbolos
symbol_table = {}

# Regla inicial
def p_program(p):
    '''
    program : include main_function
    '''
    p[0] = ('program', p[1], p[2])

# Regla para directiva #include
def p_include(p):
    '''
    include : INCLUDE HEADER
    '''
    p[0] = ('include', p[2])

# Regla para la función main
def p_main_function(p):
    '''
    main_function : INT ID LPAREN RPAREN LBRACE statements RBRACE
    '''
    p[0] = ('main_function', p[2], p[6])

# Regla para statements
def p_statements(p):
    '''
    statements : statement statements
                | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

# Regla para statement
def p_statement(p):
    '''
    statement : declaration SEMICOLON
                | assignment SEMICOLON
                | for_loop
                | RETURN expression SEMICOLON
                | expression SEMICOLON
    '''
    p[0] = p[1]

def p_declarations(p):
    '''
    declarations : declaration SEMICOLON declarations
                | declaration SEMICOLON
    '''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
# Regla para declaración
def p_declaration(p):
    '''
    declaration : type ID EQUALS expression 
    | declaration
    '''
    
    if p[2] in symbol_table:
        errores.append(f"Variable '{p[2]}' ya declarada")
    else:
        symbol_table[p[2]] = p[4]
        check_semantics(p[2], p[4])
    
    p[0] = ('declaration', p[2], p[4])


# Regla para tipo de datos
def p_type(p):
    '''
    type : INT
    '''
    p[0] = p[1]

# Regla para bucle for
def p_for_loop(p):
    '''
    for_loop : FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN LBRACE statements RBRACE
    '''
    p[0] = ('for_loop', p[3], p[5], p[7], p[10])

# Reglas para asignación, condición e incremento en el bucle for
def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    check_variable(p[1])
    check_semantics(p[1], p[3])
    p[0] = ('assignment', p[1], p[3])

def p_condition(p):
    '''
    condition : ID LEQ NUMBER
    '''
    check_variable(p[1])
    p[0] = ('condition', p[1], p[2], p[3])

def p_increment(p):
    '''
    increment : ID INCREMENT
    '''
    check_variable(p[1])
    p[0] = ('increment', p[1])

# Regla para expresión
def p_expression(p):
    '''
    expression : NUMBER
                | ID
                | expression PLUS expression
                | ID MULT NUMBER
    '''
    if len(p) == 2:
        if isinstance(p[1], str):
            check_variable(p[1])
        p[0] = p[1]
    elif len(p) == 4:
        if p[2] == '+':
            if isinstance(p[1], str):
                check_variable(p[1])
            if isinstance(p[3], str):
                check_variable(p[3])
            p[0] = ('plus', p[1], p[3])
        elif p[2] == '*':
            if isinstance(p[1], str):
                check_variable(p[1])
            if not isinstance(p[3], int):
                errores.append(f"Incompatibilidad de tipos en la expresión: {p[3]}")
            p[0] = ('mult', p[1], p[3])
            
# Verificar si una variable ha sido declarada antes de ser usada
def check_variable(var):
    if var not in symbol_table:
        errores.append(f"Variable '{var}' no declarada")

# Verificar si la asignación es semánticamente válida
def check_semantics(var, expr):
    if var in symbol_table:
        if isinstance(expr, tuple):
            if expr[0] == 'plus':
                if isinstance(expr[1], str):
                    check_variable(expr[1])
                if isinstance(expr[2], str):
                    check_variable(expr[2])
            elif expr[0] == 'mult':
                if isinstance(expr[1], str):
                    check_variable(expr[1])
                if not isinstance(expr[2], int):
                    errores.append(f"Incompatibilidad de tipos en la expresión: {expr[2]}")
        elif isinstance(expr, str):
            check_variable(expr)
    else:
        errores.append(f"Variable '{var}' no declarada antes de la asignación")

# Ejecución del árbol de parseo
def execute_statements(statements):
    for statement in statements:
        if statement[0] == 'declaration':
            for var, expr in statement[2]:
                if expr is not None:
                    symbol_table[var] = evaluate_expression(expr)
                else:
                    symbol_table[var] = 0
        elif statement[0] == 'assignment':
            symbol_table[statement[1]] = evaluate_expression(statement[2])
        elif statement[0] == 'for_loop':
            execute_for_loop(statement)
        elif statement[0] == 'return':
            return evaluate_expression(statement[1])
        else:
            evaluate_expression(statement)

def execute_for_loop(for_loop):
    initial_assignment = for_loop[1]
    condition = for_loop[2]
    increment = for_loop[3]
    statements = for_loop[4]

    # Ejecutar la asignación inicial del bucle for
    execute_assignment(initial_assignment)

    # Evaluar la condición del bucle for
    while evaluate_condition(condition):
        # Ejecutar los statement dentro del bucle for
        execute_statements(statements)

        # Ejecutar la parte de incremento
        execute_increment(increment)

def execute_assignment(assignment):
    var = assignment[1]
    expr = assignment[2]
    symbol_table[var] = evaluate_expression(expr)

def evaluate_condition(condition):
    var = condition[1]
    operator = condition[2]
    value = condition[3]

    if operator == '<=':
        return symbol_table[var] <= value
    else:
        errores.append(f"Operador no soportado: {operator}")

def execute_increment(increment):
    var = increment[1]
    symbol_table[var] += 1

def evaluate_expression(expr):
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, str):
        return symbol_table[expr]
    elif isinstance(expr, tuple):
        if expr[0] == 'plus':
            left_value = evaluate_expression(expr[1])
            right_value = evaluate_expression(expr[2])
            return left_value + right_value
        elif expr[0] == 'mult':
            left_value = evaluate_expression(expr[1])
            right_value = expr[2]
            return left_value * right_value
        else:
            errores.append(f"Operador no reconocido: {expr[0]}")
    else:
        errores.append(f"Expresión no válida: {expr}")
    
# Regla para errores de sintaxis
def p_error(p):
    if p:
        error_message = (
            f"Error de sintaxis en la posición {p.lexpos}: Token '{p.value}' inesperado"
        )
    else:
        error_message = 'Error de sintaxis: se expera un token'
    raise SyntaxError(error_message)


# Instanciar el analizador
parser = yacc.yacc()


# Función para analizar una expresión
def parse(data):
    global errores
    global symbol_table
    error_message = None  # Inicializa la variable error_message
    resultado = None  # Inicializa la variable resultado
    try:
        resultado = parser.parse(data)
        if resultado is not None:
            return str(resultado) + ' ,Sintaxis correcta'
        else:
            return 'Sintaxis correcta'

    except SyntaxError as e:
        error_message = str(e)
        print('Error:', error_message)
        return error_message