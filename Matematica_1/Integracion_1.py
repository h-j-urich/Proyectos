""" Conversión de Números: Desarrollen un programa que convierta números decimales a binarios y, 
de forma opcional, también de binario a decimal. Extensión: Validar la entrada y mostrar mensajes 
de error ante datos incorrectos. """

# Funciones de validacion de entrada: 

def validar_entrada_natural():
    num_natural = int(input("Ingrese un numero entero natural para pasarlo a binario: "))
    while num_natural < 0:  # condicion menor que cero te mantiene en el bucle
        num_natural = int(input("ERROR!, ingrese un numero entero positivo:  "))
    return num_natural

def validar_entrada_binaria():
    entrada = input("Ingrese un número binario: ") # Ingresan como cadena de texto
    while not all(caracter in "01" for caracter in entrada): # El bucle verifica que SI NO son todos "0 y 1" devuelve error.
        print("ERROR! Ingreso no válido, debe ser un número binario.")
        entrada = input("Ingrese un número binario válido: ")
    return entrada

# Función para convertir un número decimal a binario

def decimal_a_binario(numero):
    return bin(numero)[2:]  # La función bin() devuelve la representación binaria con "0b" al inicio indicando que esta 
                            # en base 2, por eso usamos [2:] para eliminar los indices 0 y 1 y dejar el numero binario puro.

# Función para convertir un número binario a decimal
def binario_a_decimal(binario):
    return int(binario, 2)  # La función int() convierte la cadena binaria a un número decimal. 
                            # El argumento 2 indica que la cadena esta en base 2.

def main():
    ejecutando = True  # Variable de control para el ciclo
    while ejecutando:
        print("\n--- Menú de Opciones ---")
        print("1. Convertir número decimal a binario")
        print("2. Convertir número binario a decimal")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num = validar_entrada_natural()
            print(f"El número binario es: {decimal_a_binario(num)}")
        elif opcion == "2":
            binario = validar_entrada_binaria()
            print(f"El número decimal es: {binario_a_decimal(binario)}")
        elif opcion == "3":
            print("Saliendo del programa...")
            ejecutando = False  # Se cambia la variable para salir del ciclo
        else:
            print("ERROR! Opción no válida. Intente nuevamente.")

# Ejecutamos la función principal si este archivo es el programa principal
if __name__ == "__main__":
    main()
