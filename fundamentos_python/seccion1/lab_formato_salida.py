# ============================================================
# LAB: Dando formato a la salida
# Sección 1 – El Programa "¡Hola, Mundo!"
# ============================================================

# Formato con separadores personalizados
print("H", "E", "L", "L", "O", sep="-")

# Formato con sep vacío (sin separador)
print("H", "E", "L", "L", "O", sep="")

# Combinación de end y sep para formatear salida en una sola línea
print("Nombre:", end=" ")
print("Monty Python", end="\n")

# Uso de \n dentro de cadenas para saltos de línea formateados
print("=== Información del estudiante ===")
print("Nombre: Juan\nEdad: 20\nCurso: Python Fundamentals")

# Doble barra invertida para mostrar una barra invertida literal
print("Ruta del archivo: C:\\Users\\Estudiante\\Python")

# Formato de tabla simple con sep
print("Nombre", "Nota", "Estado", sep="\t|\t")
print("Juan",   "4.5",  "Aprobado", sep="\t|\t")
print("Ana",    "3.8",  "Aprobado", sep="\t|\t")
