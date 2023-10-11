def sumar_numeros_impares(numbers):
    """Sum the odd numbers in a list of numbers and return the result."""
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

def lista_unicos_ordenados(numeros):
    """Devuelve una lista de elementos únicos de una lista, en el orden de la primera lista."""
    unicos = []
    for num in numeros:
        if num not in unicos:
            unicos.append(num)
    return unicos

def numeros_pares(numeros):
    """Devuelve una lista de números pares de una lista de números."""
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

def numeros_impares(numeros):
    """Devuelve una lista de números impares de una lista de números."""
    impares = []
    for num in numeros:
        if num % 2 != 0:
            impares.append(num)
    return impares


print ("\nEJERCICIO SUMAR NUMEROS IMPARES")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = sumar_numeros_impares(numeros)
print("La suma de números impares es:", resultado)

print ("\nEJERCICIO NUMEROS PARES")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = numeros_pares(numeros)
print("Números pares:", pares)


print ("\nEJERCICIO NUMEROS IMPARES")
numeros = [1, 2, 3, 4, 5, 6, 7]
unicos = numeros_impares(numeros)
print("Elementos únicos:", unicos)


print ("\nEJERCICIO LISTA UNICOS(NUMEROS NO REPETIDOS)")
numeros = [1, 6, 2, 3, 4, 4, 5, 5,2,6]
unicos = lista_unicos_ordenados(numeros)
print("Elementos únicos:", unicos)

