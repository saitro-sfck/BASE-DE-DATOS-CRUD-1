
while True:
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Ejercicio 1 - Datos personales")
    print("2. Ejercicio 2 - Tipos de datos")
    print("3. Ejercicio 3 - Operaciones básicas")
    print("4. Ejercicio 4 - Par o impar")
    print("5. Ejercicio 5 - Mayor de edad")
    print("6. Ejercicio 6 - Tabla de multiplicar")
    print("7. Ejercicio 7 - Suma del 1 al 100")
    print("11. Ejercicio 11 - Buscar el mayor")
    print("12. Ejercicio 12 - Contar pares")
    print("13. Ejercicio 13 - While básico")
    print("14. Ejercicio 14 - Validar nota")
    print("15. Ejercicio 15 - Contar vocales")
    print("16. Ejercicio 16 - Función saludar")
    print("17. Ejercicio 17 - Función suma")
    print("18. Ejercicio 18 - Diccionario simple")
    print("19. Ejercicio 19 - Recorrer diccionario")
    print("20. Ejercicio 20 - Mini reto integrador")
    print("21. Ejercicio 21 - Palindromo")

    opc = input("Elige un ejercicio a visualizar: ")

    match opc:
        case "1":
            print("EJERCICIO 1")
            NOMBRE = "Giovanni"
            edad = 18
            carrera = "Ciencia de Datos e Inteligencia Artificial"

            print("NOMBRE:", NOMBRE)
            print("EDAD:", edad)
            print("CARRERA:", carrera)

        case "2":
            print("EJERCICIO 2")
            entero = 10
            decimal = 8.5
            texto = "Python"
            activo = True
            print(type(entero))
            print(type(decimal))
            print(type(texto))
            print(type(activo))

        case "3":
            print("EJERCICIO 3")
            num1 = float(input("Ingrese un numero: "))
            num2 = float(input("Ingrese un numero: "))
            print("SUMA:", num1 + num2)
            print("RESTA:", num1 - num2)

        case "4":
            print("EJERCICIO 4")
            numero = int(input("Ingrese un numero: "))
            if numero % 2 == 0:
                print("EL NUMERO ES PAR")
            else:
                print("EL NUMERO ES IMPAR")

        case "5":
            print("EJERCICIO 5")
            edad = int(input("Ingrese un numero: "))
            if edad>=18:
                print("Es mayor de edad")
            else:
                print("Es menor de edad")

        case "6":
            print("EJERCICIO 6")
            numero = int(input("Ingrese un numero: "))
            for i in range(1,11):
                print(numero, "x", i, "=", numero * i)

        case "7":
            print("EJERCICIO 7")
            suma = 0
            for i in range(1,101):
                suma += i
            print("La suma es:", suma)

        case "8":
            numero = float(input("Ingrese un numero: "))
            if numero > 0:
                print("El numero es positivo")
            elif numero < 0:
                print("El numero es negativo")
            else:
                print("El numero es 0")

        case "9":
            print("EJERCICIO 9")
            notas = [8,9,7,10,6]
            for nota in notas:
                print("Nota:", nota)

        case "10":
            print("EJERCICIO 10")
            numeros = [4,6,8,10,12]
            promedio = sum(numeros)/len(numeros)
            print("El promedio es:", promedio)
        case "11":
            print("EJERCICIO 11")
            numeros = [12, 5, 18, 3, 20]
            mayor = max(numeros)
            print("El mayor es:", mayor)

        case "12":
            print("EJERCICIO 12")
            contador = 0
            for i in range(1, 21):
                if i % 2 == 0:
                    contador += 1
            print("Cantidad de pares:", contador)

        case "13":
            print("EJERCICIO 13")
            contador = 1
            while contador <= 5:
                print(contador)
                contador += 1

        case "14":
            print("EJERCICIO 14")
            nota = float(input("Ingrese una nota: "))
            while nota < 0 or nota > 10:
                print("Nota inválida")
                nota = float(input("Ingrese otra vez la nota: "))
            print("Nota válida:", nota)

        case "15":
            print("EJERCICIO 15")
            palabra = input("Ingrese una palabra: ")
            contador = 0
            for letra in palabra:
                if letra.lower() in "aeiou":
                    contador += 1
            print("Vocales:", contador)

        case "16":
            print("EJERCICIO 16")


            def saludar(nombre):
                print("Hola,", nombre)


            saludar("Ana")

        case "17":
            print("EJERCICIO 17")


            def sumar(a, b):
                return a + b


            resultado = sumar(5, 7)
            print("Resultado:", resultado)

        case "18":
            print("EJERCICIO 18")
            estudiante = {
                "nombre": "Luis",
                "edad": 24,
                "carrera": "Ciencia de Datos"
            }
            print(estudiante)

        case "19":
            print("EJERCICIO 19")
            persona = {"nombre": "Sara", "edad": 30, "ciudad": "Quito"}
            for clave, valor in persona.items():
                print(clave, ":", valor)

        case "20":
            print("EJERCICIO 20")
            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            n3 = float(input("Nota 3: "))

            promedio = (n1 + n2 + n3) / 3
            print("Promedio:", promedio)

            if promedio >= 7:
                print("Aprobado")
            else:
                print("Requiere refuerzo")

        case "21":
            print("EJERCICIO 21 - PALÍNDROMO")
            palabra = input("Ingresa una palabra o frase: ")
            convierte = palabra.lower().replace(" ", "")
            invertida = convierte[::-1]

            if convierte == invertida:
                print("Es un palíndromo")
            else:
                print("No es un palíndromo")




