
# LAB: La funcion print() y sus argumentos
# Seccion 1 – El Programa "¡Hola, Mundo!"


# Multiples argumentos separados por coma
print("La Witsi Witsi Araña", "subio", "a su telaraña.")

# Argumentos posicionales
print("Mi nombre es", "Python.")
print("Monty Python.")

# Argumento de palabra clave: end
# Evita el salto de linea al final
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# end vacio: no agrega nada al final
print("Mi nombre es ", end="")
print("Monty Python.")

# Argumento de palabra clave: sep
# Cambia el separador entre argumentos
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Combinando sep y end
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
