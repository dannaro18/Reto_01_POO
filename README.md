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
Se creó una función llamada "operaciones" que tiene como argumentos dos números (pueden ser decimales) y un operador (string), ingresados por el usuario (se pide que ingrese los dos números y el operador). Se utilizaron if, elif y else para establecer la operación a realizar dependiendo del operador ingresado, finalmente imprimiendo el resultado obtenido. En el caso de la división, si el segundo número es 0, se imprime "No se puede dividir entre 0", y si el operador ingresado es distinto a +, -, *, /, se imprime "El operador no es válido".


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
Se creó una función llamada "palindromo" que recibe como argumento una palabra ingresada por el usuario (se pide que ingrese la palabra). Se utiliza un ciclo while, para recorrer la palabra de inicio a fin, y viceversa, mediante la utilización de las variables "inicio" y "fin" las cuales comienzan en 0 y la longitud de la palabra, respectivamente. Se compara si el primer caracter de la palabra es diferente al último, de ser así imprimiendo "No es un palíndromo", y en caso contrario se continúa recorriendo la palabra en ambas direcciones sumando 1 a la variable "inicio" y restando 1 a la variable "fin", hasta terminar la palabra. En caso de que se cumpla el ciclo para todos los caracteres, significa que los caracteres de la palabra evaluados de inicio a fin son iguales a los caracteres evaluados de fin a inicio, imprimiendo "Sí es un palíndromo".


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
Se creó una función llamada "primo", la cual recibe como argumento un número entero. Si este número es menor o igual a 1, retorna Falso. Dentro de ella se utiliza un ciclo for en el cual se recorren los números desde el 2 hasta el número ingresado y se evalúa la división entre el número ingresado y estos números, con la condición de que si el módulo de la división es igual a 0 (es decir que el número ingresado es divisible entre el número evaluado en el ciclo), la función retorna Falso, dado que al ser divisible entre algún número desde 2 y menor a él, significa que no es primo. En caso de que termine el ciclo for y no sea divisible entre ninguno de los números, la función retorna Verdadero.
Se creó una segunda función llamada "números_primos", la cual tiene como argumento una lista de números ingresada por el usuario (se pide que ingrese la lista y se utiliza "eval" para ingresarla como lista a la función). Esta función evalúa los elementos de la lista de entrada por medio de la función "primo" y retorna los elementos para los cuales el resultado de la función es Verdadero, obteniendo una lista de números primos. Finalmente, se imprime un mensaje junto con la lista de números primos.


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
Se creó una función llamada "mayor_suma", la cual recibe como argumento una lista de números enteros ingresada por el usuario (se pide que ingrese la lista y se utiliza "eval" para ingresarla como lista a la función). Se realiza la suma entre los dos primeros elementos de la lista y se define como variable "nueva_suma". Posteriormente, se evalúa cada elemento en la lista mediante un ciclo for y se realiza la suma de este número con su consecutivo, y se compara el resultado con el valor actual de la variable "mayor_suma". En caso de que el nuevo valor sea mayor, este se guarda en la variable "mayor_suma". Una vez recorridos todos los elementos de la lista, se imprime un mensaje junto con el valor de la variable con la mayor suma entre números consecutivos.


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
Se creó una función llamada "palabras_mismos_caracteres", la cual recibe como argumento una lista de palabras ingresada por el usuario (se pide que ingrese la lista y se utiliza "eval" para ingresarla como lista a la función). Se crea una lista vacía llamada "respuesta" y mediante ciclos for se recorre la lista ingresada por el usuario, comparando el elemento evaluado con el siguiente. Estas se ponen en orden alfabético mediante la función "sorted" y se comparan; si las palabras resultan ser iguales y aún no hacen parte de la lista "respuesta", se añaden a esta mediante "append". Al terminar el ciclo, el retorno de la función es una lista que contiene las palabras con los mismos caracteres. Finalmente, se imprime un mensaje junto con la lista de palabras con los mismos caracteres. 

