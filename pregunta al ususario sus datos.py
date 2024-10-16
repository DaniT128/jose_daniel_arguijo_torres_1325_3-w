print(" ") #deja un espacio al momento de ejecutar 
print("jose daniel arguijo torres 1325 3-w")
print(" ") #deja un espacio al momeno de ejecutar 

nombre = input("Ingresa tu nombre: ") #pide tu nombre  
edad = input("Ingresa tu edad: ") #indica una edad exacta 
direccion = input("Ingresa tu dirección: ") #indica una direccion 
telefono = input("Ingresa tu número de teléfono: ") #indica un numero de telefono 

datos_personales = { #llave abierta 
    'nombre': nombre,  
    'edad': edad,           # datos personales del ususario 
    'direccion': direccion,
    'telefono': telefono
} #llave cerrada 

print(f"{datos_personales['nombre']} tiene {datos_personales['edad']} años,") #indica los datos del ususario 
print(f"vive en {datos_personales['direccion']} ") #indica la verificacion de la direccion 
print(f"y su número de teléfono es {datos_personales['telefono']}.") #indica la verificacion del numero 