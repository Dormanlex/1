
num = int(input("Ingrese un numero de mas de 2 digitos: "))

suma = 0

while num > 0:
    digito = num % 10
    suma += digito
    num //= 10

print("La suma de los dígitos es:", suma)