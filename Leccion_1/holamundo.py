# hola.py
def main():
    print("¡Hola, mundo!")
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola, {nombre}! Bienvenido a Python.")

if __name__ == "__main__":
    main()


'''
Python asigna un valor especial a la variable mágica __name__:

Si ejecutas el archivo directamente → __name__ == "__main__".

Si lo importas → __name__ == "nombre_del_archivo".
'''