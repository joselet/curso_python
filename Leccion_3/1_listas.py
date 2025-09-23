print ("listas:")
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])         # acceso: "manzana"
frutas.append("pera")    # añadir
frutas.remove("banana")  # eliminar
frutas[1] = "kiwi"       # modificar
print(frutas)

print ("slicing (rebanadas)")
nums = [0, 1, 2, 3, 4, 5]
print(nums[2:5])   # [2, 3, 4]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]

print ("slicing con el ejemplo de las frutas (ponemos más frutas y probamos)")
frutas.append("sandía")
frutas.append("melón")
frutas.append("melocotón")
frutas.append("uva")
print (frutas)
print ( "[2:5]")
print(frutas[2:5])   
print ( "[:3]")
print(frutas[:3])    
print ( "[::2]")
print(frutas[::2])   

