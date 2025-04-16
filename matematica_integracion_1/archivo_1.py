# Función para convertir un número decimal a binario
def decimal_a_binario(numero):
    return bin(numero)[2:]  # La función bin() devuelve la representación binaria con "0b" al inicio, 
                            # por eso usamos [2:] para eliminarlo.

# Función para convertir un número binario a decimal
def binario_a_decimal(binario):
    return int(binario, 2)  # La función int() convierte la cadena binaria a un número decimal usando base 2.

# Función para validar la entrada de números decimales
def validar_entrada_decimal(entrada):
    try:
        numero = int(entrada)  # Intentamos convertir la entrada a un número entero
        if numero < 0:  # Verificamos que el número sea positivo
            print("Error: Por favor ingrese un número entero positivo.")
            return None
        return numero
    except ValueError:
        print("Error: Entrada inválida, debe ser un número entero.") # Capturamos errores si la entrada no es un número válido
        return None

# Función para validar la entrada de números binarios
def validar_entrada_binaria(entrada):
    if all(caracter in "01" for caracter in entrada):  # Verificamos que cada carácter de la entrada sea '0' o '1'
        return entrada
    else:
        print("Error: Entrada inválida, debe ser un número binario válido.")  # Mensaje de error si la entrada no es binaria
        return None

# Función principal del programa
def main():
    print("Seleccione una opción:")
    print("1. Convertir decimal a binario")
    print("2. Convertir binario a decimal")

    opcion = input("Ingrese 1 o 2: ")  # Solicitamos la opción al usuario

    if opcion == "1":  # Conversión de decimal a binario
        entrada = input("Ingrese un número decimal: ")
        numero = validar_entrada_decimal(entrada)  # Validamos la entrada
        if numero is not None:  # Si la entrada es válida, realizamos la conversión
            print(f"El número {numero} en binario es {decimal_a_binario(numero)}")
    elif opcion == "2":  # Conversión de binario a decimal
        entrada = input("Ingrese un número binario: ")
        binario = validar_entrada_binaria(entrada)  # Validamos la entrada
        if binario is not None:  # Si la entrada es válida, realizamos la conversión
            print(f"El número binario {binario} en decimal es {binario_a_decimal(binario)}")
    else:
        print("Error: Opción no válida.")  # Mensaje de error si la opción ingresada no es válida

# Ejecutamos la función principal si este archivo es el programa principal
if __name__ == "__main__":
    main()
