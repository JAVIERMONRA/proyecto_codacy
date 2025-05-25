from utilidades import dividir

def saludar(nombre):
    print("Hola " + nombre)

saludar("Mundo")

# Corrección: manejo de división por cero
a = 10
b = 0
resultado = dividir(a, b)
print(resultado)
