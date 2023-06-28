lista = []

while True:
    num = int(input("Ingrese un numero entero (0 para salir): "))
    
    if num == 0:
        break
    
    lista.append(num)

print("Numeros ingresados:", lista)

sumatoria = sum(lista)
print("La suma de los numeros es de: ", sumatoria)

cantidad = len(lista)
promedio = sumatoria/cantidad
print("El promedio de los numeros ingresados es de: ", promedio)
