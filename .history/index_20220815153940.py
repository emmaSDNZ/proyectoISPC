number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
number4 = int(input("Ingresa el cuarto número: "))
number5 = int(input("Ingresa el quinto número: "))


# 1) El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.
lista = [number1, number2, number3, number4, number5]

# 2) Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.
def sumar_list(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

# 3) Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.
def promedio (lista) : 
    suma = 0
    for i in range(lista):
        suma += lista[i]
    return suma/len(lista)

    
# 4)Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.
def num_Maximo (lista) :
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

#5) Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.
def num_Minimo (lista):
    min = value[0]
    for i in range(1, len(lista)):
        if lista[i] < min :
            min = lista[i]
    return min



value = int(input('Por favor, elija un numero: \n '
 """
    1. Función Suma
    2. Función Promedio
    3. Función Máximo
    4. Función Mínimo
    """))

if value == 1: 
    print("La suma total es: " ,sumar_list(lista))
    
elif value == 2 : 
    print("El promedio total es: " ,promedio (lista))

elif value == 3 : 
    print("El numero maximo es: " ,num_Maximo (lista))

elif value == 4 : 
    print("El numero minimo es: " ,num_Minimo (lista))
else:  
    print("el numero no es correcto")    


