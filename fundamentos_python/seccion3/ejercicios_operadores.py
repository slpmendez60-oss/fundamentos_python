# ============================================================
# Ejercicios de Operadores Matemáticos
# Sección 3 – Operadores: herramientas de manipulación de datos
# ============================================================

print("=" * 55)
print("   EJERCICIOS DE OPERADORES MATEMÁTICOS EN PYTHON")
print("=" * 55)

# ---- 1. SUMA (+) ----
print("\n--- Suma (+) ---")
print("2 + 3        =", 2 + 3)          # int + int = int
print("-4 + 4       =", -4 + 4)         # resultado: 0
print("-4.0 + 8     =", -4.0 + 8)       # float + int = float
print("100 + 200    =", 100 + 200)

# ---- 2. RESTA (-) ----
print("\n--- Resta (-) ---")
print("10 - 3       =", 10 - 3)         # int - int = int
print("-4 - 4       =", -4 - 4)         # resultado: -8
print("4.0 - 8      =", 4.0 - 8)        # float - int = float
print("-1.1         =", -1.1)           # operador unario negativo

# ---- 3. MULTIPLICACIÓN (*) ----
print("\n--- Multiplicación (*) ---")
print("2 * 3        =", 2 * 3)          # int * int = int
print("2 * 3.0      =", 2 * 3.0)        # int * float = float
print("2.0 * 3      =", 2.0 * 3)        # float * int = float
print("2.0 * 3.0    =", 2.0 * 3.0)      # float * float = float

# ---- 4. DIVISIÓN (/) ----
print("\n--- División (/) ---")
print("6 / 3        =", 6 / 3)          # SIEMPRE devuelve float
print("6 / 3.0      =", 6 / 3.0)
print("6.0 / 3      =", 6.0 / 3)
print("7 / 2        =", 7 / 2)          # resultado: 3.5

# ---- 5. DIVISIÓN ENTERA (//) ----
print("\n--- División Entera (//) ---")
print("6 // 3       =", 6 // 3)         # int // int = int
print("6 // 3.0     =", 6 // 3.0)       # int // float = float
print("6.0 // 3     =", 6.0 // 3)
print("6 // 4       =", 6 // 4)         # resultado: 1 (redondea abajo)
print("6.0 // 4     =", 6.0 // 4)
print("-6 // 4      =", -6 // 4)        # redondeo hacia abajo: -2
print("6.0 // -4    =", 6.0 // -4)      # redondeo hacia abajo: -2.0

# ---- 6. MÓDULO / RESIDUO (%) ----
print("\n--- Módulo / Residuo (%) ---")
print("14 % 4       =", 14 % 4)         # 14 // 4 = 3, 3*4=12, 14-12=2
print("12 % 4.5     =", 12 % 4.5)       # resultado: 3.0
print("5 % 2        =", 5 % 2)          # resultado: 1
print("9 % 3        =", 9 % 3)          # resultado: 0 (divisible exacto)

# ---- 7. EXPONENCIACIÓN (**) ----
print("\n--- Exponenciación (**) ---")
print("2 ** 3       =", 2 ** 3)         # int ** int = int: 8
print("2 ** 3.0     =", 2 ** 3.0)       # int ** float = float: 8.0
print("2.0 ** 3     =", 2.0 ** 3)
print("2.0 ** 3.0   =", 2.0 ** 3.0)
print("3E8          =", 3E8)            # notación científica

# ---- 8. PRIORIDADES Y PARÉNTESIS ----
print("\n--- Prioridades de Operadores ---")
# La precedencia: ** > unarios > *, /, //, % > +, -
print("2 + 3 * 5             =", 2 + 3 * 5)            # 17, no 25
print("(2 + 3) * 5           =", (2 + 3) * 5)          # 25
print("2 * 3 % 5             =", 2 * 3 % 5)            # (2*3)%5 = 6%5 = 1
print("9 % 6 % 2             =", 9 % 6 % 2)            # izq→der: (9%6)%2 = 3%2 = 1
print("2 ** 2 ** 3           =", 2 ** 2 ** 3)          # der→izq: 2**(2**3) = 2**8 = 256
print("-3 ** 2               =", -3 ** 2)              # -(3**2) = -9
print("-(3 ** 2)             =", -(3 ** 2))            # también -9
print("5 * ((25%13)+100)/(2*13)//2 =",
      (5 * ((25 % 13) + 100) / (2 * 13)) // 2)         # resultado: 10.0

# ---- 9. APLICACIÓN: TEOREMA DE PITÁGORAS ----
print("\n--- Aplicación: Teorema de Pitágoras ---")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print(f"Cateto a = {a}")
print(f"Cateto b = {b}")
print(f"Hipotenusa c = √(a² + b²) =", c)

# ---- 10. APLICACIÓN: ÁREA Y PERÍMETRO ----
print("\n--- Aplicación: Área y Perímetro de un rectángulo ---")
base = 8
altura = 5
area = base * altura
perimetro = 2 * (base + altura)
print(f"Base     = {base}")
print(f"Altura   = {altura}")
print(f"Área     = base × altura = {area}")
print(f"Perímetro = 2 × (base + altura) = {perimetro}")

print("\n" + "=" * 55)
print("   FIN DE LOS EJERCICIOS DE OPERADORES")
print("=" * 55)
