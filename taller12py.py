import math

a = 0.45
x = 0.455
verdadero = math.exp(-x)

for n in range(16):
    aprox = 0
    for i in range(n+1):
        derivada = (-1)**i * math.exp(-a)
        aprox += (derivada / math.factorial(i)) * ((x-a)**i)
    error_relativo = abs((verdadero - aprox) / verdadero) * 100
    print(f"Orden {n}: {aprox:.6f}, Error relativo porcentual: {error_relativo:.6f}%")
