# 🐍 Fundamentos de Python – GA1-220501093-04-AA1-EV01

Repositorio del proyecto de fundamentos de Python. Contiene los scripts de cada laboratorio de las Secciones 1 a 4, más la solución completa de los ejercicios de operadores matemáticos.

---

## 📁 Estructura del Repositorio

```
fundamentos_python/
├── src/
│   └── puntaje_final_jugador.py        ← Proyecto integrador
├── seccion1/
│   ├── lab_print_basico.py
│   ├── lab_print_argumentos.py
│   └── lab_formato_salida.py
├── seccion2/
│   └── lab_literales_cadenas.py
├── seccion3/
│   └── ejercicios_operadores.py
├── seccion4/
│   ├── lab_variables.py
│   ├── lab_convertidor_simple.py
│   └── lab_operadores_expresiones.py
└── README.md
```

---

## ▶️ Cómo ejecutar los programas

Requisitos: Python 3.6 o superior instalado.

```bash
# Ejemplo: ejecutar cualquier script
python seccion1/lab_print_basico.py
python seccion3/ejercicios_operadores.py
python src/puntaje_final_jugador.py
```

---

## 📚 Sección 1 – El Programa "¡Hola, Mundo!"

### Conceptos cubiertos
- La función `print()` y cómo envía texto a la consola.
- Argumentos posicionales y de palabra clave (`end`, `sep`).
- Caracteres de escape (`\n`, `\\`).
- Invocación de funciones en Python.

### Scripts
| Archivo | Descripción |
|---|---|
| `lab_print_basico.py` | Primer programa, saltos de línea, `\n` |
| `lab_print_argumentos.py` | Múltiples argumentos, `end` y `sep` |
| `lab_formato_salida.py` | Formato de tabla, separadores personalizados |

---

## 📚 Sección 2 – Literales de Python

### Conceptos cubiertos
- Qué es un **literal**: dato cuyo valor está determinado por sí mismo.
- Tipos de literales: **enteros**, **flotantes**, **cadenas**, **booleanos**, `None`.
- Números octales (`0o`) y hexadecimales (`0x`).
- Notación científica (`3E8`, `6.62607E-34`).
- Cadenas con comillas dobles, simples y caracteres de escape.

### Scripts
| Archivo | Descripción |
|---|---|
| `lab_literales_cadenas.py` | Todos los tipos de literales en Python |

---

## 📚 Sección 3 – Operadores Matemáticos

> **Esta sección contiene la solución completa de los ejercicios de operadores, con explicación de lógica y ejemplos de salida.**

### Operadores disponibles en Python

```
+   -   *   /   //   %   **
```

---

### 1. Suma `+`

**Lógica:** Une dos valores. Si alguno es flotante, el resultado es flotante.

```python
print(2 + 3)       # → 5
print(-4 + 4)      # → 0
print(-4.0 + 8)    # → 4.0
```

**Salida:**
```
5
0
4.0
```

---

### 2. Resta `-`

**Lógica:** Sustrae el valor derecho del izquierdo. El signo `-` también funciona como operador unario para negar un número.

```python
print(10 - 3)      # → 7
print(-4 - 4)      # → -8
print(4.0 - 8)     # → -4.0
print(-1.1)        # → -1.1  (unario)
```

**Salida:**
```
7
-8
-4.0
-1.1
```

---

### 3. Multiplicación `*`

**Lógica:** Multiplica dos valores. Sigue la regla `int * int = int`; si alguno es flotante, el resultado es flotante.

```python
print(2 * 3)       # → 6
print(2 * 3.0)     # → 6.0
print(2.0 * 3)     # → 6.0
print(2.0 * 3.0)   # → 6.0
```

**Salida:**
```
6
6.0
6.0
6.0
```

---

### 4. División `/`

**Lógica:** **Siempre devuelve flotante**, sin importar si los operandos son enteros.

```python
print(6 / 3)       # → 2.0  (no 2)
print(7 / 2)       # → 3.5
print(6 / 3.0)     # → 2.0
```

**Salida:**
```
2.0
3.5
2.0
```

---

### 5. División Entera `//`

**Lógica:** Divide y **redondea hacia abajo** al entero inferior más cercano (*floor division*). Con enteros devuelve entero; con flotantes devuelve flotante.

```python
print(6 // 3)      # → 2
print(6 // 4)      # → 1   (no 1.5)
print(6.0 // 4)    # → 1.0
print(-6 // 4)     # → -2  (redondeo hacia abajo, no hacia cero)
print(6.0 // -4)   # → -2.0
```

**Salida:**
```
2
1
1.0
-2
-2.0
```

> ⚠️ **Importante:** `-6 // 4` no es `-1`, es `-2` porque el redondeo siempre va hacia el entero **inferior** (más negativo).

---

### 6. Módulo / Residuo `%`

**Lógica:** Devuelve el **residuo** de la división entera. Útil para verificar divisibilidad, ciclos, y más.

**Fórmula:** `a % b = a - (a // b) * b`

```python
print(14 % 4)      # → 2   (14//4=3, 3*4=12, 14-12=2)
print(5 % 2)       # → 1
print(9 % 3)       # → 0   (divisible exacto)
print(12 % 4.5)    # → 3.0
```

**Salida:**
```
2
1
0
3.0
```

---

### 7. Exponenciación `**`

**Lógica:** Eleva la base a la potencia del exponente. Usa **enlazado del lado derecho** (se evalúa de derecha a izquierda).

```python
print(2 ** 3)        # → 8
print(2 ** 3.0)      # → 8.0
print(2 ** 2 ** 3)   # → 256  (2**(2**3) = 2**8)
print(-3 ** 2)       # → -9   (-(3**2), no (-3)**2)
print(3E8)           # → 300000000.0
```

**Salida:**
```
8
8.0
256
-9
300000000.0
```

---

### 8. Prioridad de Operadores

La jerarquía de mayor a menor prioridad es:

| Prioridad | Operador | Descripción |
|:---------:|----------|-------------|
| 1 | `**` | Exponenciación (enlace derecho) |
| 2 | `+x`, `-x` | Unarios |
| 3 | `*`, `/`, `//`, `%` | Multiplicación y división |
| 4 | `+`, `-` | Suma y resta binarias |

```python
print(2 + 3 * 5)              # → 17  (no 25)
print((2 + 3) * 5)            # → 25
print(2 * 3 % 5)              # → 1   ((2*3)%5 = 6%5)
print(9 % 6 % 2)              # → 1   (izq→der: (9%6)%2)
print((5*((25%13)+100)/(2*13))//2)  # → 10.0
```

**Salida:**
```
17
25
1
1
10.0
```

---

### 9. Aplicación – Teorema de Pitágoras

```python
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
```

**Salida:**
```
c = 5.0
```

---

## 📚 Sección 4 – Variables

### Conceptos cubiertos
- Variables como contenedores de datos con nombre y valor.
- Reglas de nomenclatura (PEP 8): `snake_case`, sin espacios, sin palabras reservadas.
- Creación automática al asignar valor: `var = 1`.
- Operadores de asignación compuesta: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
- Sensibilidad a mayúsculas: `var` ≠ `Var`.

### Scripts
| Archivo | Descripción |
|---|---|
| `lab_variables.py` | Creación, uso y operadores abreviados |
| `lab_convertidor_simple.py` | Convertidor km↔millas, °C↔°F, horas→segundos |
| `lab_operadores_expresiones.py` | Expresiones combinadas con variables |

---

## 🎮 Proyecto Integrador – `src/puntaje_final_jugador.py`

Script que integra todos los conceptos: variables, literales, y los siete operadores aritméticos para calcular el puntaje final de un jugador.

**Ejemplo de salida:**
```
==================================================
     RESULTADO FINAL DEL JUGADOR
==================================================
Jugador        : Python Gamer
Puntos base    : 1500
Bonus nivel x3 : 4500
Penalización   : -200
Bonus vidas    : +300
--------------------------------------------------
PUNTAJE FINAL  : 4600
Porcentaje     : 92.0 %
Nivel alcanzado: 4
Pts hacia nivel 5 : 400 pts restantes
==================================================
```

---

## 👤 Información del Estudiante

- **Actividad:** GA1-220501093-04-AA1-EV01
- **Tema:** Fundamentos de Python: variables, operadores y manipulación de cadenas
- **Secciones:** 1, 2, 3 y 4
