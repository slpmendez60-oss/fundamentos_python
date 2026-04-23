# ============================================================
# LAB: Literales de Python - Cadenas
# Sección 2 – Literales de Python
# ============================================================

# --- LITERALES NUMÉRICOS ---

# Entero vs cadena: print los muestra igual, pero son tipos distintos
print("2")   # cadena (string)
print(2)     # entero (integer)

# Enteros con guión bajo para legibilidad (Python 3.6+)
print(11111111)
print(11_111_111)   # mismo valor, más legible

# Números negativos y positivos
print(-11_111_111)
print(+11111111)

# Números octales (prefijo 0o)
print(0o123)   # equivale a 83 en decimal

# Números hexadecimales (prefijo 0x)
print(0x123)   # equivale a 291 en decimal

# --- FLOTANTES ---
print(2.5)
print(-0.4)
print(.4)      # el cero antes del punto es opcional
print(4.)      # el cero después del punto es opcional

# Notación científica
print(3E8)          # velocidad de la luz: 300,000,000
print(6.62607E-34)  # Constante de Planck

# Python elige la representación más corta
print(0.0000000000000000000001)   # muestra: 1e-22

# --- CADENAS ---

# Comillas dobles
print("Yo soy una cadena.")

# Escapando comillas dentro de cadenas
print("Me gusta \"Monty Python\"")

# Usando apóstrofes como delimitador alternativo
print('Me gusta "Monty Python"')

# Escapando apóstrofe dentro de cadena con apóstrofes
print('I\'m Monty Python.')

# --- BOOLEANOS ---
print(True)
print(False)

# Los booleanos se comportan como 1 y 0 numéricamente
print(True > False)   # True (1 > 0)
print(True < False)   # False (1 < 0)

# --- NONE ---
print(None)   # representa la ausencia de valor
