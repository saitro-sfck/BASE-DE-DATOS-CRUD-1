import math

print("CALCULADORA CIENTIFICA")
while True:
    print("\n Escoja la operacion a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Seno (en grados)")
    print("8. Coseno (en grados)")
    print("9. Tangente (en grados)")
    print("10. Logaritmo base 10")
    print("11. Logaritmo natural")
    print("12. Factorial")
    print("0. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")
    if opcion == "0":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    try:
        if opcion in ["1","2","3","4","5"]:
            num1 = float(input("Ingrese el primer número: "))
            num2= float(input("Ingrese el segundo numero: "))

            if opcion == "1":
                resultado = num1 + num2
            elif opcion == "2":
                resultado = num1 - num2
            elif opcion == "3":
                resultado = num1 * num2
            elif opcion == "4":
                resultado = num1/num2
            else: 
                resultado = num1 ** num2
        elif opcion in ["6","7","8","9","10","11","12"]:
            num = float(input("Ingrese el número: "))
            if opcion == "6":
                resultado = math.sqrt(num)
            elif opcion == "7" :
                resultado= math.sin(math.radians(num))
            elif opcion == "8":
                resultado= math.cos(math.radians(num))
            elif opcion == "9":
                resultado= math.tan(math.radians(num))
            elif opcion == "10":
                resultado= math.log10(num)
            elif opcion == "11":
                resultado= math.log(num)
            elif opcion == "12":
                resultado= math.factorial(int(num))

        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            continue
        print("El resultado es:", resultado)

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
    except ValueError:
        print("Error: entrada inválida o fuera del dominio de la función")

        

        



        

