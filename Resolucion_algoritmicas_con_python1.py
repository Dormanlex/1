while True:
    num = input("Ingrese un numero entero (para salir ingrese *): ")
    if num == "*":
        break
    
    num = int(num)
    
    if num > 0:
        print("El numero es positivo.")
    elif num < 0:
        print("El numero es negativo.")
    else:
        print("El numero es igual a 0.")