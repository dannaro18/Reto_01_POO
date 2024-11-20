# Reto 1 - Programación Orientada a Objetos

## 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.

```python
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
```
### Explicación
aaa


## 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
```python
def palindromo(palabra: str):
    inicio = 0
    fin = len(palabra) - 1
    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return "No es un palíndromo"  
        inicio = inicio + 1
        fin = fin - 1
    return "Sí es un palíndromo"  

palabra = str(input("Ingresa la palabra"))
print(palindromo(palabra))
```
### Explicación
aaa


## 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
def primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def numeros_primos(numeros: list) -> list:
    return [num for num in numeros if primo(num)]

numeros = eval(input("Ingresa la lista de números enteros"))

print("Los números primos son: " + str(numeros_primos(numeros)))
```
### Explicación
aaa


## 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
def mayor_suma(numeros: list):
    mayor_suma = numeros[0] + numeros[1]
    for i in range(1, len(numeros) - 1):
        nueva_suma = numeros[i] + numeros[i + 1]
        if nueva_suma > mayor_suma:
            mayor_suma = nueva_suma
    return mayor_suma

numeros = eval(input("Ingresa la lista de números enteros"))
print("La mayor suma de números consecutivos es: " + str(mayor_suma(numeros)))
```
### Explicación
aaa


## 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
```python
def palabras_mismos_caracteres(palabras: list) -> list:
    respuesta = []
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if sorted(palabras[i]) == sorted(palabras[j]) and palabras[i] not in respuesta:
                respuesta.append(palabras[i])
                respuesta.append(palabras[j])
    return respuesta
    
palabras = eval(input("Ingresa la lista de palabras"))
print("Las palabras con los mismos caracteres son: " + str(palabras_mismos_caracteres(palabras)))
```
### Explicación
aaa

