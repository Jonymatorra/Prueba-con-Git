print("todo bien") 


print(" *Menu de opciones* ")  


print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo o resto\n")

numero = int(input("Introduce la opcion deseada: "))

if numero == 1:

    print("Elejiste suma\n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ",numero)
    

elif numero == 2:

    print("Elejiste resta\n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ",numero)

elif numero == 3:

    print("Elejiste multiplicacion\n")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es: ",numero)

elif numero == 4:

    print("Elejiste division\n")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la division es: ",round(numero,2))

elif numero == 5:

    print("Elejiste division entera\n")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la division entera es: ",numero)

elif numero == 6:

    print("Elejiste exponente\n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado del exponente es: ",numero)

elif numero == 7:

    print("Elejiste modulo o resto\n")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El resultado del modulo es: ",numero)

else:
    print("La opcion elejida no existe, vuelve a intentar.")



