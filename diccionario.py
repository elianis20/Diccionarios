#DICCIONARIOS 

hi_army = {"Nombre": "Nini",
            "Apellido": "Madero",
            "Fan": "BTS"}


print("Mi nombre:", hi_army ["Nombre"] )
print("Mi apellido:", hi_army ["Apellido"])
print("Soy fan de:", hi_army ["Fan"])




Coders = {
1: {
      "Nombre": "Elianis",
      "Apellido": "Cervnates",
      "id": "1043585751"
      },

2: {
      "Nombre": "Deyanis",
      "Apellido": "Martero",
      "id": "130586333"
            },
      
3: {
      "Nombre": "Angela",
      "Apellido": "Manjares",
      "id": "10564745"
      },
      }


opcion = 0 
while opcion != 4: 

      print(" ===== MENU DE CODERS=====")
      print("1. Agregar coder")
      print("2. Buscar coder")
      print("3. Eliminar coder")
      print("4. Salir")

      opcion = input("Elige una opcion: ")
# AGREGAR      

if opcion == "1": 
      id_coder = int(input("Ingresa el documento: "))
      nombre = input("Ingresa tu nombre: ")
      apellido = input("Ingresa tu apellido")

      Coders [1] = {
            "id": id_coder,
            "nombre": nombre,
            "apellido": apellido
      }

print(f"Coder {nombre} {apellido} agregado con exito")

#BUESCAR

elif opcion == "2": 

