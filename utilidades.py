# Funciones matemáticas básicas

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"  # Buena práctica detectada
    return a / b

def operacion_innecesaria(x):
    if x > 0:
        return True
    else:
        return True  # Codacy debe marcar esto como code smell
