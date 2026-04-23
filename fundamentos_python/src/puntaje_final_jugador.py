# ============================================================
# puntaje_final_jugador.py
# Proyecto: Fundamentos de Python
# Calcula el puntaje final de un jugador usando operadores
# ============================================================

# Datos del jugador (variables)
nombre_jugador = "Python Gamer"
puntos_base    = 1500
bonus_nivel    = 3        # multiplicador de nivel
penalizacion   = 200      # puntos perdidos por errores
vidas_extra    = 2

# ---- Cálculo del puntaje ----

# 1. Puntos con bonus de nivel (multiplicación)
puntos_con_bonus = puntos_base * bonus_nivel

# 2. Descontar penalización (resta)
puntos_netos = puntos_con_bonus - penalizacion

# 3. Bonus por vidas extra: cada vida extra vale 150 pts (suma)
bonus_vidas = vidas_extra * 150
puntos_finales = puntos_netos + bonus_vidas

# 4. Calcular porcentaje sobre puntaje máximo posible (división)
puntaje_maximo = 5000
porcentaje = (puntos_finales / puntaje_maximo) * 100

# 5. Nivel de clasificación usando división entera y módulo
nivel_alcanzado = puntos_finales // 1000
residuo_nivel   = puntos_finales % 1000

# ---- Mostrar resultados ----
print("=" * 50)
print("     RESULTADO FINAL DEL JUGADOR")
print("=" * 50)
print("Jugador        :", nombre_jugador)
print("Puntos base    :", puntos_base)
print("Bonus nivel x" + str(bonus_nivel) + " :", puntos_con_bonus)
print("Penalización   : -" + str(penalizacion))
print("Bonus vidas    : +" + str(bonus_vidas))
print("-" * 50)
print("PUNTAJE FINAL  :", puntos_finales)
print("Porcentaje     :", round(porcentaje, 2), "%")
print("Nivel alcanzado:", nivel_alcanzado)
print("Pts hacia nivel", nivel_alcanzado + 1, ":", 1000 - residuo_nivel, "pts restantes")
print("=" * 50)
