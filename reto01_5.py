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


