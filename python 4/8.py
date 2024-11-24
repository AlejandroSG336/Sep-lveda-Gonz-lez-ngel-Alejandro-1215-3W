def contar_nombres_por_letra():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una letra y una lista de nombres
    separados por espacios. Cuenta cuántos nombres comienzan con la letra especificada.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    letra = input("Ingrese la letra a buscar: ")
    nombres = input("Ingrese una lista de nombres separados por espacios: ").split()
    cantidad = sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))
    print(f"Cantidad de nombres que comienzan con '{letra}':", cantidad)

contar_nombres_por_letra()
