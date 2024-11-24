def contar_vocales():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una palabra y cuenta
    cuántas veces aparece cada vocal en la palabra.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiou"
    conteo = {vocal: palabra.lower().count(vocal) for vocal in vocales}
    print("Conteo de vocales:", conteo)

contar_vocales()
