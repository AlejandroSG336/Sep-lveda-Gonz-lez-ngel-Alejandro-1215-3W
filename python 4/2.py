def mas_larga():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una lista de palabras 
    separadas por espacios y devuelve la palabra más larga.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
    print("La palabra más larga es:", max(palabras, key=len))

mas_larga()
