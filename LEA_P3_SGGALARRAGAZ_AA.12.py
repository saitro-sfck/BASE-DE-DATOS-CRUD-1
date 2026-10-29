#(Sistema de reservaciones de una aerolínea) Una pequeña aerolínea acaba de comprar una
#computadora para su nuevo sistema de reservaciones automatizado. Se le ha pedido a usted que
#desarrolle el nuevo sistema. Usted escribirá una aplicación para asignar asientos en cada vuelo del
#único avión de la aerolínea (capacidad: 10 asientos).

#Su aplicación debe mostrar las siguientes alternativas: Por favor escriba 1 para Primera Clase y Por
#favor escriba 2 para Económico. Si el usuario escribe 1, su aplicación debe asignarle un asiento en
#la sección de primera clase (asientos 1 a 5). Si el usuario escribe 2, su aplicación debe asignarle un
#asiento en la sección económica (asientos 6 a 10). Su aplicación deberá entonces imprimir un pase
#de abordaje, indicando el número de asiento de la persona y si se encuentra en la sección de primera
#clase o clase económica del avión.

#Use un arreglo unidimensional del tipo primitivo boolean para representar la tabla de asientos del
#avión. Inicialice todos los elementos del arreglo con false para indicar que todos los asientos están
#vacíos. A medida que se asigne cada asiento, establezca los elementos correspondientes del
#arreglo en true para indicar que ese asiento ya no está disponible.

#Su aplicación nunca deberá asignar un asiento que ya haya sido asignado. Cuando este llena la
#sección económica, su programa deberá preguntar a la persona si acepta ser colocada en la sección
#de primera clase (y viceversa). Si la persona acepta, haga la asignación de asiento apropiada. Si no
#acepta, imprima el mensaje "El próximo vuelo sale en 3 horas".

asientos = [False, False, False, False, False, False, False, False, False, False]
ejecutando = True

while ejecutando:

    lleno = True
    for asiento in asientos:
        if not asiento:
            lleno = False

    if lleno:
        print("\n--- El avión está completamente lleno. No hay más reservaciones disponibles. ---")
        ejecutando = False
        continue

    print("\n*** BIENVENIDO AL SISTEMA DE RESERVACIONES ***")
    print("Por favor escriba 1 para Primera Clase")
    print("Por favor escriba 2 para Económico")
    print("Por favor escriba 3 para Salir del sistema")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 3:
        print("Saliendo del sistema...")
        ejecutando = False

    elif opcion == 1:
        asiento_asignado = -1

        for i in range(0, 5):
            if not asientos[i]:
                asientos[i] = True
                asiento_asignado = i + 1
                break

        if asiento_asignado != -1:
            print("\n========================================")
            print("          PASE DE ABORDAJE              ")
            print(f" Asiento Número: {asiento_asignado}")
            print(" Sección: Primera Clase")
            print("========================================")
        else:
            print("\nLa sección de Primera Clase está llena.")
            aceptar = input("¿Acepta ser colocado en la sección Económica? (S/N): ")

            if aceptar.lower() == 's':
                asiento_eco = -1
                for i in range(5, 10):
                    if not asientos[i]:
                        asientos[i] = True
                        asiento_eco = i + 1
                        break

                if asiento_eco != -1:
                    print("\n========================================")
                    print("          PASE DE ABORDAJE              ")
                    print(f" Asiento Número: {asiento_eco}")
                    print(" Sección: Clase Económica")
                    print("========================================")
                else:
                    print("\nLo sentimos, la sección Económica también está llena.")
                    print("El próximo vuelo sale en 3 horas.")
            else:
                print("\nEl próximo vuelo sale en 3 horas.")

    elif opcion == 2:
        asiento_asignado = -1

        for i in range(5, 10):
            if not asientos[i]:
                asientos[i] = True
                asiento_asignado = i + 1
                break

        if asiento_asignado != -1:
            print("\n========================================")
            print("          PASE DE ABORDAJE              ")
            print(f" Asiento Número: {asiento_asignado}")
            print(" Sección: Clase Económica")
            print("========================================")
        else:
            print("\nLa sección Económica está llena.")
            aceptar = input("¿Acepta ser colocado en la sección de Primera Clase? (S/N): ")

            if aceptar.lower() == 's':
                asiento_primera = -1
                for i in range(0, 5):
                    if not asientos[i]:
                        asientos[i] = True
                        asiento_primera = i + 1
                        break

                if asiento_primera != -1:
                    print("\n========================================")
                    print("          PASE DE ABORDAJE              ")
                    print(f" Asiento Número: {asiento_primera}")
                    print(" Sección: Primera Clase")
                    print("========================================")
                else:
                    print("\nLo sentimos, la sección de Primera Clase también está llena.")
                    print("El próximo vuelo sale en 3 horas.")
            else:
                print("\nEl próximo vuelo sale en 3 horas.")

    else:
        print("Opción inválida. Por favor, intente de nuevo.")










