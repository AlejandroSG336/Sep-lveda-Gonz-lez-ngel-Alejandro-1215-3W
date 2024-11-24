def contar_edades_mayores():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario diez edades y cuenta
    cuántas de ellas son mayores a 20.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    edades = [int(input("Ingrese una edad: ")) for _ in range(10)]
    mayores_de_20 = sum(1 for edad in edades if edad > 20)
    print("Cantidad de personas con edades mayores a 20:", mayores_de_20)

contar_edades_mayores()
