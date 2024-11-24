def es_bisiesto():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario un año y determina
    si es un año bisiesto. Un año es bisiesto si es divisible por 4, pero no por 100,
    excepto si es divisible por 400.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    anio = int(input("Ingrese un año: "))
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print(anio, "es un año bisiesto.")
    else:
        print(anio, "no es un año bisiesto.")

es_bisiesto()
