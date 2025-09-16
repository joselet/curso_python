#tipos basicos
a = 10         # int
b = 3.14       # float
s = "hola"     # str
flag = True    # bool

print(type(a), type(b), type(s), type(flag))


# conversion
edad = int(input("Edad: "))
print(f"El año que viene tendrás {edad + 1} años.")


#listas y diccionarios
nums = [1, 2, 3]
persona = {"nombre": "Jose", "edad": 30}
for n in nums:
    print(n)

print(persona["nombre"])
print(f"{persona["edad"]} años")
