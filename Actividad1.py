# Función que determina el mensaje según la edad (Punto #1)
def determinarMensajeEdad(edad):
    """
    Determina el mensaje personalizado según la edad del usuario:
    - Menores de 18: "Eres menor de edad"
    - Entre 18 y 65: "Eres mayor de edad"
    - Mayores de 65: "Eres una persona de la tercera edad"

    Args:
        edad (int): Edad del usuario
    Returns:
        str: Mensaje correspondiente según la edad
    """
    if edad < 18:
        mensaje = "Eres menor de edad"
    elif edad <= 65:
        mensaje = "Eres mayor de edad"
    else:
        mensaje = "Eres una persona de la tercera edad"
    print(mensaje)
    return mensaje

# Función para obtener y validar la edad del usuario (Punto #2)
def obtenerEdadValida():
    """
    Solicita al usuario ingresar su edad y valida que sea un número entero.
    Si la entrada no es válida, muestra error y vuelve a solicitar la edad.

    Returns:
        int: Edad validada como número entero
    """
    while True:
        try:
            edad = input("Ingresa tu edad: ")
            return int(edad)  # Convierte la entrada a entero
        except ValueError:
            # Si hay error en la conversión, muestra mensaje de error
            print("Error: Debes ingresar un número entero válido.")


# Función que muestra la comida favorita (Punto #3)
def mostrarComidaFavorita():
    """
    Crea una variable con el nombre de la comida favorita y la muestra en pantalla.
    Returns:
        str: El nombre de la comida favorita
    """
    comida_favorita = "Paella"
    print(f"Mi comida favorita es: {comida_favorita}")
    return comida_favorita


# Función que muestra el dinero en la billetera (Punto #4)
def mostrarDineroBilletera():
    """
    Crea una variable con la cantidad de dinero en la billetera y la muestra en pantalla.
    Returns:
        float: Cantidad de dinero en la billetera
    """
    dinero_billetera = 150.50
    print(f"Tengo ${dinero_billetera} en mi billetera")
    return dinero_billetera


# Función que muestra el gusto por el clima caliente (Punto #5)
def climaCaliente():
    """
        Crea una variable booleana para determinar el gusto por el clima calido y lo muestra en pantalla.
        Returns:
            clima_caliente: True (gusto por el clima caliente) y 
            False (disgusto por el clima caliente)
    """
    clima_caliente = True
    if clima_caliente:
        print(f"Me gusta el clima caliente")
    else:
        print(f"No me gusta el clima caliente")
    
    return clima_caliente


# Función principal que ejecuta todo el programa
def main():
    """
    Función principal que ejecuta todas las partes del programa en secuencia.
    """

    # Puntos 1 y 2: Solicitar edad y mostrar mensaje personalizado
    edad = obtenerEdadValida()
    determinarMensajeEdad(edad)

    # Puntos 3 y 4: Mostrar comida favorita y dinero en billetera
    mostrarComidaFavorita()
    mostrarDineroBilletera()

    # Punto 5: Indica si me gusta o no el clima calido
    climaCaliente()


# Punto de entrada del programa
if __name__ == "__main__":
    main()