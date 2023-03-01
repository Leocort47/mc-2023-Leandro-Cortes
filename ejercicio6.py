import math

x = float(input("Ingrese un valor en radianes: "))
eps = float(input("Ingrese el criterio de error esperado: "))

cos = 1
term = 1
error = eps + 1
n = 0

while error > eps:
    n += 1
    term *= (-1) * x * x / ((2 * n - 1) * (2 * n))
    cos += term
    error = abs(term / cos)

cos = round(cos, 8)
error_b = round(error * 100, 8)

print(f"Coseno de {x}: {cos}. Error relativo: {error_b} %, Iteraciones: {n}")