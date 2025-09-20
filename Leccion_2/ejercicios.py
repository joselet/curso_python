'''
Ejercicio 1 — Listas
Crea una lista con tus comidas favoritas. Añade 2 más, elimina 1 y muestra la lista final.

Ejercicio 2 — Diccionarios
Crea un diccionario con nombre, edad y ciudad.
Luego pídele al usuario su profesión y añádela al diccionario. Imprímelo.

Ejercicio 3 — Conjuntos
Pide al usuario 5 números.
Guárdalos en un conjunto y muestra cuántos números únicos introdujo.

Ejercicio 4 — Comprensiones
Genera una lista con los cuadrados de los números pares del 1 al 20 usando comprensión de listas.

Ejercicio 5 — Mini proyecto
Un diccionario de estudiantes:
Pide nombres y notas hasta que el usuario escriba "fin".
Al final muestra:
- Lista de estudiantes con su nota.
- Nota media.
- El mejor estudiante.
'''
print ("ejercicio 1")
comidas = ["canelones","croquetas","ensalada"]
print (comidas)
comidas.append("tortilla")
comidas.append("bravas")
comidas.remove("ensalada")
print (comidas)

input ("pulsa enter para ejercicio 2 ")
diccionario = {
    "nombre": "Jose",
    "edad": "51",
    "ciudad": "Barcelona"
}
print (diccionario)
diccionario["profesion"]=input("Dame la profesión: ")
print(diccionario)