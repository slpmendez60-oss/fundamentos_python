# ============================================================
# LAB: Operadores y expresiones
# Sección 4 – Variables
# ============================================================

# Expresiones con variables
i = 4
j = 5
var = 2
rem = 3

# Operadores abreviados
i += 2 * j           # i = i + 2*j = 4 + 10 = 14
print("i += 2*j  → i =", i)

var /= 2             # var = var / 2 = 2 / 2 = 1.0
print("var /= 2  → var =", var)

rem %= 10            # rem = rem % 10 = 3 % 10 = 3
print("rem %= 10 → rem =", rem)

j -= (i + var + rem) # j = j - (14+1.0+3) = 5 - 18 = -13
print("j -= (i+var+rem) → j =", j)

x = 2
x **= 2              # x = x ** 2 = 4
print("x **= 2   → x =", x)

# Calculando el área de un círculo
radio = 5
PI = 3.14159
area_circulo = PI * radio ** 2
print("\nÁrea del círculo con radio", radio, "=", area_circulo)

# Calculando potencias sucesivas de 2
potencia = 1
potencia *= 2
print("\nPotencias de 2:")
print(potencia)
potencia *= 2
print(potencia)
potencia *= 2
print(potencia)
potencia *= 2
print(potencia)
