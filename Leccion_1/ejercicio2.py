from datetime import date
nombre = input("Nombre: ")
edad = int(input("Edad: "))
anio_nac = date.today().year - edad
print(f"{nombre}, naciste aproximadamente en {anio_nac}.")
