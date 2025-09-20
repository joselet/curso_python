#lists
cuadrados = [x**2 for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25]

#dict
numeros = {x: x**2 for x in range(4)}
print(numeros)  # {0: 0, 1: 1, 2: 4, 3: 9}

#set
pares = {x for x in range(10) if x % 2 == 0}
print(pares)  # {0, 2, 4, 6, 8}
