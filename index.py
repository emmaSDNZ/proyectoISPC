#EJERCICIO 1 DE PROGRAMACION INICIAL
# Se leen cinco números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
number4 = int(input("Ingresa el cuarto número: "))
number5 = int(input("Ingresa el quinto número: "))
# Se calcula la suma y el promedio de los numeros ingresados
suma = number1 + number2 + number3 + number4 + number5
promedio = suma / 5
# Verifica cuál de los números es el mayor y menor
numeroMasGrande = max(number1, number2, number3, number4, number5)
numeroMasChico = min(number1, number2, number3, number4, number5)
# Imprime el resultado.
print("")
print("El número más grande es:", numeroMasGrande)
print(f'El numero mas chico es: {numeroMasChico}')
print(f'La suma de los numeros es: {suma}')
print(f'El promedio de la suma es: {promedio}')
