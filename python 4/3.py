def filtrar_palabras():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una lista de palabras
    separadas por espacios y un número entero. Devuelve las palabras con más de 'n' caracteres.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
    n = int(input("Ingrese un número entero: "))
    resultado = [palabra for palabra in palabras if len(palabra) > n]
    print("Palabras con más de", n, "caracteres:", resultado)

filtrar_palabras()
