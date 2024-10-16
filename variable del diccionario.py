print(" ") #para dejar un espacio al momeno de ejecutar 
print("jose daniel arguijo torres 1325 3-w")
print(" ") #para dejar un espacio al momento de ejecutar 

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'} #para identificar el simbolo de divisas 

entrada = input("Ingresa una divisa (Euro, Dollar, Yen): ") #pide el ingreso de una divisa 

if entrada in divisas: #identifica la divisa 
    print(f"El símbolo de {entrada} es: {divisas[entrada]}") #pide identificar el simbolo de divisa 
else: #cierre del programa 
    print("La divisa no está en el diccionario.") #indica que no esta dentro del programa 