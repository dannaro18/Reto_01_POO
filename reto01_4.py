def mayor_suma(numeros: list):
    mayor_suma = numeros[0] + numeros[1]
    for i in range(1, len(numeros) - 1):
        nueva_suma = numeros[i] + numeros[i + 1]
        if nueva_suma > mayor_suma:
            mayor_suma = nueva_suma
    return mayor_suma

numeros = eval(input("Ingresa la lista de números enteros"))
print("La mayor suma de números consecutivos es: " + str(mayor_suma(numeros)))