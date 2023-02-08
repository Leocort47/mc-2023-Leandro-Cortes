a = {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
b = {0,2,4,6,8,10,12,14,16,18,20,22,24}
c = {1,4,8,10,12,15,18,20}
d = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}


def union(a, b):
     u = a|b
     return u

def interseccion(a, b):
    i = a&b
    return i


def diferencia(a, b):
    i = a-b
    return i


def diferenciaSimetrica(a,b):
    d = a^b
    return d

op1 = interseccion(b, diferenciaSimetrica(c, d))
print(op1)

#u = (a&c)|b
op2 = union(interseccion(a,c), b)
print(op2)

#i = (b|d)-c
op3 = diferencia(union(b,d),c)
print(op3)

#d = (a-b)^(a&d) 
op4 = diferenciaSimetrica(diferencia(a,b), interseccion(a,d))
print(op4)



       