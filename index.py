
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
number4 = int(input("Ingresa el cuarto número: "))
number5 = int(input("Ingresa el quinto número: "))


arr = [number1, number2, number3, number4, number5]

def numMaximo (value) : 
    max = value[0]
    for i in range(1, len(value)):
        if value[i] > max:
            max = value[i]
    return max

print ("funcion Numero Maximo", numMaximo(arr))