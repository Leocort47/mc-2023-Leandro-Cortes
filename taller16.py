import math

# Definir las variables X y Y
X = [0, 1, 2, 3, 4, 5, 6, 7]
Y = [3.5, 2.5, 3, 1.5, 2, 1.3, 1, 0.3]

# Calcular la media de X y Y
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# Calcular la desviación estándar de X y Y
std_dev_x = math.sqrt(sum([(x - mean_x)**2 for x in X]) / (len(X) - 1))
std_dev_y = math.sqrt(sum([(y - mean_y)**2 for y in Y]) / (len(Y) - 1))

# Calcular el coeficiente de correlación r
r = sum([(x - mean_x) * (y - mean_y) for x, y in zip(X, Y)]) / \
    ((len(X) - 1) * std_dev_x * std_dev_y)

# Calcular la pendiente m y el intercepto b de la línea de regresión
m = r * (std_dev_y / std_dev_x)
b = mean_y - (m * mean_x)

# Imprimir la ecuación de la línea de regresión
print(
    "La ecuación de la línea de regresión es: y = {:.2f}x + {:.2f}".format(m, b))
