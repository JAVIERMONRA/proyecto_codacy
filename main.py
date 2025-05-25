def saludar(nombre):
    print("Hola " + nombre)

def dividir(a, b):
    return a / b  # Posible división por cero

def innecesario(x):
    if x > 0:
        return True
    else:
        return True  # Condicional innecesaria

saludar("Mundo")
print(dividir(10, 0))  # Esto causa error en ejecución, pero Codacy lo marca como riesgo
