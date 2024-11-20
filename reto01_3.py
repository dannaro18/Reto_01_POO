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