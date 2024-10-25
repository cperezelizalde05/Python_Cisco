# while True:
#     print("Estoy atrapado dentro de un bucle.")

# Almacena el actual número más grande aquí.
# largest_number = -999999999

# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))

# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))

# # Imprime el número más grande.
# print("El número más grande es:", largest_number)


################################################################################
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

# odd_numbers = 0
# even_numbers = 0

# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

#####################################################################

# counter = 5
# while counter:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

#####################################################################
#Ejercicio
# secret_number = 777
# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)
# while secret_number:
#     numero_elegido = int(input("Adivina el número secreto "))
#     if numero_elegido == secret_number:
#         print("¡Bien hecho, muggle! Eres libre ahora.")
#         break
#     else:
#         print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

######################################################################
# #Ejemplo For/Range
# for i in range(2, 8):
#     print("El valor de i es", i)

#####################################################################
#Ejercicio If/Elif/Else n°1
# entrada = input("Ingresar el nombre de tu planta favorita: ")
# if entrada == "ESPATIFILIO":
#     print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
# elif entrada == "espatifilio":
#     print("No, ¡quiero un gran Espatifilo!")
# else:
#     print(f"¡Espatifilo!, ¡No {entrada}!")


#Ejercicio If/Elif/Else n°2
# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# # Escribe tu código aquí.
# else:
#     excedente = income - 85528
#     tax = 14839.02 + (excedente * 0.32)
# if tax < 0:
#     tax = 0.0
# tax = round(tax, 0)
# print("El impuesto es:", tax, "pesos")

#Ejercicio n°3
# year = int(input("Introduce un año: "))

# if year < 1582:
# 	print("No esta dentro del período del calendario Gregoriano")
# else:
#     if year % 4 != 0:
#         print ("Año común")
#     elif year % 100 != 0:
#         print("Año bisiesto")
#     elif year % 400 != 0:
#         print("Año común")
#     else:
#         print("Año bisiesto")

#Ejercicio for
# import time

# for i in range(1,6):
#     print(f"{i} Mississippi")
#     time.sleep(1)
# print("¡Listos o no, ahí voy!")

########################################################################
#Ejemplos de Break y continue
# break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# if counter:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

#Ejercicio n°1 Break/Continue

# while True:
#     palabra = input("Ingrese una palabra: ")
#     if palabra == "chupacabra":
#         print("Has dejado el bucle con éxito.")
#         break

#Ejercicio n°2 Break/Continue
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
# user_word = input("Por favor escribir una palabra: ")
# user_word = user_word.upper()
# for letter in user_word:
#     if letter in ("A","E","I","O","U"):
#         continue
#     word_without_vowels = letter
#     print(word_without_vowels)
#Ejercicio n°1 While
# blocks = int(input("Ingresa el número de bloques: "))

# height = 0
# bloques_usados = 0
# bloques_necesarios = 1

# # Mientras tengamos suficientes bloques para construir otra capa
# while bloques_usados + bloques_necesarios <= blocks:
#     height += 1
#     bloques_usados += bloques_necesarios
#     bloques_necesarios += 1 

# print("La altura de la pirámide:", height)

#Ejercicio n°2
# Leer el número natural inicial
# c0 = int(input("Ingresa un número natural: "))

# # Asegurarse de que el número sea positivo
# if c0 <= 0:
#     print("El número debe ser un entero positivo.")
# else:
#     # Inicializar contador de pasos
#     pasos = 0
    
#     # Mientras c0 sea diferente de 1
#     while c0 != 1:
#         print(c0)  # Mostrar el valor intermedio
        
#         # Si es par, dividir entre 2
#         if c0 % 2 == 0:
#             c0 = c0 // 2
#         # Si es impar, calcular 3 * c0 + 1
#         else:
#             c0 = 3 * c0 + 1
        
#         # Incrementar el contador de pasos
#         pasos += 1
    
#     # Mostrar el último valor (que siempre será 1)
#     print(c0)
    
#     # Mostrar el número de pasos
#     print("Pasos totales:", pasos)

# n = range(4)

# for num in n:
#     print(num - 1)
# else:
#     print(num)

# Ejemplos de Operadores lógicos
# var = 17
# var_right = var >> 1
# var_left = var << 1
# print(var, var_left, var_right)

#Ejemplos listas
# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

# numbers[0] = 111
# print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

#Ejercicio n°1 - LISTAS
# hat_list = [1, 2, 3, 4, 5]
# print(hat_list)
# num_user = int(input("Ingresar un número que reemplace el número central. Debe ser un número entero "))
# hat_list [2] = num_user #el número ingresado reemplaza el número central.
# print(hat_list)
# del hat_list[-1] #elimina el último elemento de la lista
# print(hat_list)
# print("La nueva longitud de la lista es de ", len(hat_list)) #imprrime la nueva longitud de la lista. 

#Bucle for ejemplo

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)

# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)

#Ejercicio Bucles
# beatles = []
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison") #agregar miempros
# print("Paso 2:", beatles)

# for miembro in ["Stu Sutcliffe", "Pete Best"]:
#     beatles.append(input(f"Por favor agregar a {miembro} a la lista: "))
# print("Paso 3:", beatles)

# del beatles[-2:]
# print("Paso 4:", beatles)

# beatles.insert(0, "Ringo Starr")
# print("Paso 5:", beatles)


