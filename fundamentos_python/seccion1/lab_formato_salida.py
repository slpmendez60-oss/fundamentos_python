
# LAB: Dando formato a la salida
# Seccion 1 – El Programa "¡Hola, Mundo!"

# Formato con separadores personalizados
print("H", "E", "L", "L", "O", sep="-")

# Formato con sep vacio (sin separador)
print("H", "E", "L", "L", "O", sep="")

# Combinacion de end y sep para formatear salida en una sola linea
print("Nombre:", end=" ")
print("Monty Python", end="\n")

# Uso de \n dentro de cadenas para saltos de linea formateados
print("=== Informacion del estudiante ===")
print("Nombre: Luis\nEdad: 20\nCurso: Python Fundamentals")

# Doble barra invertida para mostrar una barra invertida literal
print("Ruta del archivo: C:\\Users\\Estudiante\\Python")

# Formato de tabla simple con sep
print("Nombre", "Nota", "Estado", sep="\t|\t")
print("Luis",   "4.5",  "Aprobado", sep="\t|\t")
print("Ana",    "3.8",  "Aprobado", sep="\t|\t")
