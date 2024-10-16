print(" ") #para dejar un espacio al momento de ejecutar 
print("jose daniel arguijo torres 1325 3-w")
print(" ") #para dejar un espacio al momento de ejecutar  

precios_frutas = { #indica el valor de cada fruta 
    'manzana': 2.5,  # precio por kilo
    'plátano': 3.0,
    'naranja': 1.8,
    'uva': 4.0
} #cierre de llaves 

fruta = input("Ingresa el nombre de la fruta: ").lower()  #indica el nombre de una fruta 
kilos = float(input("Ingresa el número de kilos: ")) #indica el numero de kilos 

if fruta in precios_frutas: #valor de la fruta 
    precio_total = precios_frutas[fruta] * kilos #indica el precio 
    print(f"El precio total por {kilos} kilos de {fruta} es: ${precio_total:.2f}") #indica el precio final de la fruta 
else: #cierre del programa 
    print("La fruta no está en el diccionario.") #indica que no esta en el programa 