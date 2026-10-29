
# INTEGRANTES DEL GRUPO:
# 1. [Nombre del Integrante 1: Steven Cuti
# 2. [Nombre del Integrante 2: Katherin Melendres
# 3. [Nombre del Integrante 3: Esteban Pazmiño

print("Seleccione una opción para ejecutar el programa:")
print("1. Control de límite de crédito de clientes")
print("2. Cálculo de ingresos semanales de vendedores")
print("3. Cálculo de sueldo bruto de tres empleados")
print("=========================================================")

opcion = input("Ingrese el número de la opción que desea (1, 2 o 3): ")

match opcion:

    # --------------------------------------------------------------------------
    # CASE 1: CONTROL DE LÍMITE DE CRÉDITO
    # --------------------------------------------------------------------------
    case "1":
        print("\n--- EJECUTANDO: CONTROL DE LÍMITE DE CRÉDITO ---")

        num_cuenta = int(input("Ingrese el número de cuenta: "))
        saldo_inicial = int(input("Ingrese el saldo al inicio del mes: "))
        cargos = int(input("Ingrese el total de artículos cargados en el mes: "))
        creditos = int(input("Ingrese el total de créditos aplicados en el mes: "))
        limite_credito = int(input("Ingrese el límite de crédito permitido: "))

        nuevo_saldo = saldo_inicial + cargos - creditos

        print("\n---------------- RESET DE CUENTA ----------------")
        print(f"Número de cuenta: {num_cuenta}")
        print(f"Saldo inicial: {saldo_inicial}")
        print(f"Total de cargos: {cargos}")
        print(f"Total de créditos: {creditos}")
        print(f"Nuevo saldo: {nuevo_saldo}")
        print(f"Límite de crédito permitido: {limite_credito}")
        print("-------------------------------------------------")

        if nuevo_saldo > limite_credito:
            print("Mensaje: Se excedió el límite de su crédito")
        else:
            print("Mensaje: El cliente se encuentra dentro del límite de crédito permitido.")

    # --------------------------------------------------------------------------
    # CASE 2: INGRESOS SEMANALES DE VENDEDORES
    # --------------------------------------------------------------------------
    case "2":
        print("\n--- EJECUTANDO: INGRESOS SEMANALES DE VENDEDORES ---")

        print("\n================ CATÁLOGO DE ARTÍCULOS ================")
        print("Artículo 1: $239.99")
        print("Artículo 2: $129.75")
        print("Artículo 3: $99.95")
        print("Artículo 4: $350.89")
        print("=======================================================")

        ventas_brutas = 0.0

        print("\nIngrese la cantidad vendida de cada artículo durante la semana:")

        cant_art1 = int(input("Cantidad vendida del Artículo 1: "))
        ventas_brutas = ventas_brutas + (cant_art1 * 239.99)

        cant_art2 = int(input("Cantidad vendida del Artículo 2: "))
        ventas_brutas = ventas_brutas + (cant_art2 * 129.75)

        cant_art3 = int(input("Cantidad vendida del Artículo 3: "))
        ventas_brutas = ventas_brutas + (cant_art3 * 99.95)

        cant_art4 = int(input("Cantidad vendida del Artículo 4: "))
        ventas_brutas = ventas_brutas + (cant_art4 * 350.89)

        salario_base = 200.00
        comision = ventas_brutas * 0.09
        ingreso_total = salario_base + comision

        print("\n---------------- RESUMEN DE INGRESOS ----------------")
        print(f"Total de ventas brutas: ${ventas_brutas:.2f}")
        print(f"Valor de la comisión obtenida (9%): ${comision:.2f}")
        print(f"Salario base semanal: ${salario_base:.2f}")
        print(f"Ingreso total del vendedor: ${ingreso_total:.2f}")
        print("-----------------------------------------------------")

    # --------------------------------------------------------------------------
    # CASE 3: SUELDO BRUTO DE TRES EMPLEADOS
    # --------------------------------------------------------------------------
    case "3":
        print("\n--- EJECUTANDO: SUELDO BRUTO DE EMPLEADOS ---")


        # --- EMPLEADO 1 ---
        print("\n--- Datos del Empleado 1 ---")
        nombre1 = input("Nombre del empleado: ")
        horas1 = float(input("Número de horas trabajadas: "))
        tarifa1 = float(input("Tarifa de pago por hora: "))

        if horas1 <= 40:
            sueldo1 = horas1 * tarifa1
        else:
            sueldo1 = (40 * tarifa1) + ((horas1 - 40) * tarifa1 * 1.5)

        # --- EMPLEADO 2 ---
        print("\n--- Datos del Empleado 2 ---")
        nombre2 = input("Nombre del empleado: ")
        horas2 = float(input("Número de horas trabajadas: "))
        tarifa2 = float(input("Tarifa de pago por hora: "))

        if horas2 <= 40:
            sueldo2 = horas2 * tarifa2
        else:
            sueldo2 = (40 * tarifa2) + ((horas2 - 40) * tarifa2 * 1.5)

        # --- EMPLEADO 3 ---
        print("\n--- Datos del Empleado 3 ---")
        nombre3 = input("Nombre del empleado: ")
        horas3 = float(input("Número de horas trabajadas: "))
        tarifa3 = float(input("Tarifa de pago por hora: "))

        if horas3 <= 40:
            sueldo3 = horas3 * tarifa3
        else:
            sueldo3 = (40 * tarifa3) + ((horas3 - 40) * tarifa3 * 1.5)

        # --- MOSTRAR RESULTADOS GENERALES ---
        print("\n================ REPORTE DE SUELDOS BRUTOS ================")

        print(f"Empleado: {nombre1}")
        print(f"  Horas trabajadas: {horas1}")
        print(f"  Tarifa por hora: ${tarifa1:.2f}")
        print(f"  Sueldo bruto calculado: ${sueldo1:.2f}")
        print("-" * 45)

        print(f"Empleado: {nombre2}")
        print(f"  Horas trabajadas: {horas2}")
        print(f"  Tarifa por hora: ${tarifa2:.2f}")
        print(f"  Sueldo bruto calculado: ${sueldo2:.2f}")
        print("-" * 45)

        print(f"Empleado: {nombre3}")
        print(f"  Horas trabajadas: {horas3}")
        print(f"  Tarifa por hora: ${tarifa3:.2f}")
        print(f"  Sueldo bruto calculado: ${sueldo3:.2f}")
        print("===========================================================")

    case _:
        print("\n[ERROR]: Opción inválida. Por favor, ejecute el programa de nuevo y seleccione 1, 2 o 3.")


