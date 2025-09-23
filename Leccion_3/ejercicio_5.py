alumnos = []
nombre = ""
while nombre != "fin":
    nombre = input("Introduce un nombre de alumno ('fin' para acabar):")
    if nombre != "fin":
        nota = float(input(f"Introduce la nota de {nombre}: "))
        alumnos.append({"nombre":nombre, "nota":nota})

numalumnos=0
maxnota=0
sum=0
for alumno in alumnos:    
    numalumnos+=1
    sum+=alumno["nota"]
    ganador =""
    if alumno["nota"]>maxnota:
        maxnota=alumno["nota"]
        ganador=alumno["nombre"]
    print(f"Alumno: {alumno['nombre']}, Nota: {alumno['nota']}")
print(f"Nota promedio; {sum/numalumnos}")
print(f"Nota máxima: {maxnota} de {ganador}")
