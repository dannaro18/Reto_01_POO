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