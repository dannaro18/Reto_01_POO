def operaciones(a: float, b: float, operador: str):
    if operador == "+":
        return a+b
    elif operador == "-":
        return a-b
    elif operador == "*":
        return a*b
    elif operador == "/":
        if b == 0:
            return "No se puede dividir entre 0"
        else:
            return a/b
    else:
        return "El operador no es válido"

a = float(input("Ingresa el primer número"))
b = float(input("Ingresa el segundo número"))
operador = str(input("Ingresa el operador"))
print(operaciones(a, b, operador))