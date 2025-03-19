# Paso 1: Solicitar al usuario que ingrese el radio del círculo.

import math

radio = float(input("Por favor, ingrese el radio del círculo: "))

# Paso 2: Calcular el área del círculo utilizando la fórmula: area = π*radio^2

area = math.pi*(radio**2)

# Paso 3: Mostrar al usuario el area calculada

print("El área del círculo de radio", radio, "es:", area)3

# Resultado redondeado

area_redondeada = round(area, 2)

print("El área redondeada del círculo de radio", radio, "es:", area_redondeada)