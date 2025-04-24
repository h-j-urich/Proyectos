#!/bin/bash

# Pedimos la extensión
read -p "Extensión del archivo (sin el punto, por ejemplo 'txt'): " extension

# Se buscan los archivos
for archivo in *."$extension"; do
    # Se verifica si existe
    if [ -e "$archivo" ]; then
        echo "Nombre del archivo: $archivo"
        cat $archivo
        echo "============================================"
    fi
done

