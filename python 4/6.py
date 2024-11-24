def calcular_edades():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita el año en curso y los nombres
    y años de nacimiento de tres personas. Calcula cuántos años cumplirán en el año actual.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    anio_actual = int(input("Ingrese el año en curso: "))
    for _ in range(3):
        nombre = input("Ingrese el nombre de la persona: ")
        anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
        edad = anio_actual - anio_nacimiento
        print(f"{nombre} cumplirá {edad} años durante el año en curso.")

calcular_edades()
