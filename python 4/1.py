def max_in_list():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una lista de números
    separados por espacios y devuelve el número más grande.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    numeros = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [float(num) for num in numeros]  # Conversión a float para admitir decimales
    print("El número más grande es:", max(numeros))

max_in_list()
