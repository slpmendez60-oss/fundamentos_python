# ============================================================
# LAB: La función print() y sus argumentos
# Sección 1 – El Programa "¡Hola, Mundo!"
# ============================================================

# Múltiples argumentos separados por coma
print("La Witsi Witsi Araña", "subió", "a su telaraña.")

# Argumentos posicionales
print("Mi nombre es", "Python.")
print("Monty Python.")

# Argumento de palabra clave: end
# Evita el salto de línea al final
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# end vacío: no agrega nada al final
print("Mi nombre es ", end="")
print("Monty Python.")

# Argumento de palabra clave: sep
# Cambia el separador entre argumentos
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Combinando sep y end
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
