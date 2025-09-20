persona = {"nombre": "Ana", "edad": 30}
print(persona["nombre"])        # Ana
persona["edad"] = 31            # modificar
persona["ciudad"] = "Madrid"    # añadir
print(persona)

#recorrido
for clave, valor in persona.items():
    print(clave, ":", valor)
