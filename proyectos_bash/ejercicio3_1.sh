#!/bin/bash

# Pedimos la ruta del archivo
read -p "Ingrese la ruta del archivo: " archivo 

# Verificamos que exista
if [ -e "$archivo" ]; then
    echo "El archivo $archivo existe"

    # Se verifica el tipo de archivo
    if [ -b "$archivo" ]; then
        echo "Es un archivo especial de bloques"
    elif [ -c "$archivo" ]; then
        echo "Es un archivo especial de caracteres"
    elif [ -d "$archivo" ]; then
        echo "Es un directorio"
    elif [ -f "$archivo" ]; then
        echo "Es un archivo ordinario"
    elif [ -h "$archivo" ]; then
        echo "Es un enlace simbólico"
    else
        echo "Es otro tipo de archivo"
    fi

    # Se muestran los permisos
    [ -r "$archivo" ] && echo "Tiene permiso de lectura"
    [ -w "$archivo" ] && echo "Tiene permiso de escritura"
    [ -x "$archivo" ] && echo "Tiene permiso de ejecución"

else
    echo "El archivo $archivo no existe"
fi

