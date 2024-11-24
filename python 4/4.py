def contar_mayusculas():
    """
    Imprime el nombre, matrícula y grupo. Luego, solicita al usuario una cadena y 
    cuenta la cantidad de letras mayúsculas en ella.
    """
    print("Sepúlveda González Ángel Alejandro, 1215, 3W")
    cadena = input("Ingrese una cadena: ")
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    print("La cantidad de letras mayúsculas es:", mayusculas)

contar_mayusculas()
