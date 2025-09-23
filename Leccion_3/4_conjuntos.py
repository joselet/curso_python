colores = {"rojo", "verde", "azul"}
colores.add("rojo")   # ignorado (ya está)
print(colores)

#operaciones utiles
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # unión {1,2,3,4,5}
print(a & b)  # intersección {3}
print(a - b)  # diferencia {1,2}
