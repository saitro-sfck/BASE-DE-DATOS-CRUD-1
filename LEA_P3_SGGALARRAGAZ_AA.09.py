#Construir un programa en Python que realice las siguientes opciones
#1. Dado una entrada n, calcule la suma de los términos de una progresión aritmética como la que se
#muestra a continuación: 10, 15, 20, 25, 30, … , 𝑇𝑛. Esto es, su algoritmo debe calcular el valor:
#10 + 15 + 20 + 25 + 30 + … + 𝑇�


#Como datos el número de orden y sueldo de cada empleado, debe imprimirse el
#2. Para una empresa con N empleados, se desarrolla un algoritmo donde se ingresa
#número de orden del empleado con el mayor sueldo, así como su sueldo.
#El programa deberá repetirse hasta que se elija la opción salir.
opc=int(input("1. Calcular suma de los terminos de una progresion aritmetica\n2. Conocer el sueldo de cada empleado con su numero de orden\n Escoja una opcion:"))

match opc:
    case 1:
        n = int(input("Ingrese la cantidad de terminos de la progresion que desea calcular:"))
        suma=0
        terminoact= 10

        for i in range (n):
            suma= suma + terminoact
            terminoact= terminoact + 5

            print(f" La suma de los primeros {n} terminos a calcular es {suma}")
    case 2:
        continuar = True
        while continuar:
            print ("      SISTEMA DE ORDEN EN FUNCION AL SUELDO DE LOS EMPLEADOS       ")
            print("1. Conocer el mayor sueldo de un empleado ")
            print("2. Salir")
            opc= input("Ingrese la opcion que desea realizar:")
            if opc == "2":
                print("Saliendo del programa...")
                continuar= False
            elif opc == "1":
                n=int(input("Ingrese el numero de empleados que desea calcular:"))
                sueldomayor=0
                ordenmejor_emp=0
                for i in range (n):
                    print(f"\nDatos del empleado {i+1}:")
                    numorden= int(input("Ingrese el numero de orden del empleado:"))
                    sueldo= float(input("Ingrese el sueldo del empleado:"))
                if sueldo>sueldomayor:
                    sueldomayor=sueldo
                    ordenmejor_emp= numorden
                    print("\n========================================")
                    print(f"El empleado con el mayor sueldo es el número de orden: {ordenmejor_emp}")
                    print(f"Su sueldo es de: ${sueldomayor:.2f}")
                    print("========================================")
            else:
                print("Ingreso incorrecto, intente de nuevo...")

















