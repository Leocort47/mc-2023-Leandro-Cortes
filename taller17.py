import math
import numpy as np

# Definir las variables X y Y
X = [2, 4, 6, 8, 10, 12]
Y = [2.2, 3, 4.5, 6, 8.5, 12]

# Opción para seleccionar el tipo de modelo
modelo = input("Seleccione el tipo de modelo (1 = lineal, 2 = exponencial): ")

if modelo == "1":
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
    print("La ecuación de la línea de regresión es: y = {:.2f}x + {:.2f}".format(m, b))

elif modelo == "2":
    # Aplicar el modelo exponencial
    log_Y = [math.log(y) for y in Y]
    p = np.polyfit(X, log_Y, 1)
    a = math.exp(p[1])
    b = p[0]

    # Imprimir la ecuación de la curva exponencial
    print("La ecuación de la curva exponencial es: y = {:.2f} * exp({:.2f}x)".format(a, b))

else:
    print("Opción inválida")
