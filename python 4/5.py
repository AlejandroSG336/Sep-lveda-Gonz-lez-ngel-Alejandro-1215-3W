def binario_a_entero():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario un número en formato binario
    y lo convierte a un número entero.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    binario = input("Ingrese un número en binario: ")
    entero = int(binario, 2)
    print("El número en entero es:", entero)

binario_a_entero()
