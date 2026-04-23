# ============================================================
# LAB: Variables
# Sección 4 – Variables
# ============================================================

# --- Crear y usar variables ---
var = 1
print(var)

# Reasignar un nuevo valor
var = var + 1
print(var)

# Múltiples variables de distintos tipos
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

# Combinando texto y variables con el operador +
python_version = "3.8.5"
print("Python version: " + python_version)

# Predecir el resultado de reasignación
var2 = 100
var2 = 200 + 300
print(var2)   # resultado: 500

# --- Operadores abreviados ---
x = 10
x += 5      # x = x + 5
print("x += 5  →", x)

x -= 3      # x = x - 3
print("x -= 3  →", x)

x *= 2      # x = x * 2
print("x *= 2  →", x)

x /= 4      # x = x / 4
print("x /= 4  →", x)

x //= 2     # x = x // 2
print("x //= 2 →", x)

x **= 2     # x = x ** 2
print("x **= 2 →", x)

rem = 17
rem %= 10   # rem = rem % 10
print("17 %= 10 →", rem)

# --- Teorema de Pitágoras con variables ---
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
