//crear un programa de computador que solicite al usuario dos grupos
//de numeros decimales(dos conjuntos), pregunte la operacion que se desea
//realizar entre los conjuntos(union, interseccion, diferencia o diferencia simetrica)
//y proceda a escribir en pantalla el conjunto resultante junto con su cardinalidad

grupo1 = int(input("Digita el numero de elementos para el grupo 1: "))
s= set()
k = set()
union = set()
interseccion = set()
diferencia = set()
simetrica = set()


for i in range (0,grupo1):
    n = float(input("Digita un numero: "))
    s.add(n)

grupo2 = float(input("Digita el numero de elementos para el grupo 2: "))

for i in range (0,grupo1):
    n = float(input("Digita un numero: "))
    k.add(n)   

print("----------------------------------------")
numero = int(print("Digita la operacion que deseas realizar"))
print("1. union")
print("2. interseccion")
print("3. diferencia")
print("4. simetrica")

if numero == 1:
    
    print(s+n)


if numero == 2:
    c = s&k
    print("interseccion: "+c)

if numero == 3:
    d= s-n
    print("diferencia: "+d)

if numero ==4:
    print(s^k)


else:
    print("Error!!!")        





