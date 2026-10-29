ventas_mes = [
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0]
]

# Ingreso de datos
num_reportes = int(input("Ingrese cantidad de reportes: "))

for r in range(num_reportes):
    # Validacion del vendedor con indicador numerico
    vendedor_valido = 0
    while vendedor_valido == 0:
        vendedor = int(input("Vendedor (1-4): "))
        if vendedor >= 1 and vendedor <= 4:
            vendedor_valido = 1
        else:
            print("Vendedor no valido")

    # Validacion del producto con indicador numerico
    producto_valido = 0
    while producto_valido == 0:
        producto = int(input("Producto (1-5): "))
        if producto >= 1 and producto <= 5:
            producto_valido = 1
        else:
            print("Producto no valido")

    valor_venta = float(input("Valor de venta ($): "))
    ventas_mes[vendedor - 1][producto - 1] += valor_venta

# Menu de opciones
opcion = 0
while opcion != 5:
    print("\n1. Ventas por vendedor")
    print("2. Ventas por producto")
    print("3. Ventas totales del mes")
    print("4. Premios e incentivos")
    print("5. Salir")
    opcion = int(input("Seleccione opcion: "))

    if opcion == 1:
        # Calcular y mostrar ventas por cada vendedor
        for i in range(4):
            suma_vendedor = 0.0
            for j in range(5):
                suma_vendedor += ventas_mes[i][j]
            print(f"Vendedor {i + 1}: ${suma_vendedor:.2f}")

    elif opcion == 2:
        # Calcular y mostrar ventas por cada producto
        for j in range(5):
            suma_producto = 0.0
            for i in range(4):
                suma_producto += ventas_mes[i][j]
            print(f"Producto {j + 1}: ${suma_producto:.2f}")

    elif opcion == 3:
        # Calcular y mostrar el total general del mes
        total_general = 0.0
        for i in range(4):
            for j in range(5):
                total_general += ventas_mes[i][j]
        print(f"Total general: ${total_general:.2f}")

    elif opcion == 4:
        # Determinar el mejor, el peor y los vendedores restantes
        totales_vendedores = [0.0, 0.0, 0.0, 0.0]
        for i in range(4):
            for j in range(5):
                totales_vendedores[i] += ventas_mes[i][j]

        mejor_valor = totales_vendedores[0]
        peor_valor = totales_vendedores[0]
        id_mejor = 0
        id_peor = 0

        for i in range(1, 4):
            if totales_vendedores[i] > mejor_valor:
                mejor_valor = totales_vendedores[i]
                id_mejor = i
            if totales_vendedores[i] < peor_valor:
                peor_valor = totales_vendedores[i]
                id_peor = i

        restantes = []
        for i in range(4):
            if i != id_mejor and i != id_peor:
                restantes.append(i)

        # Asignar tarjetas de oro y plata entre los vendedores intermedios
        if len(restantes) == 2:
            if totales_vendedores[restantes[0]] >= totales_vendedores[restantes[1]]:
                oro = restantes[0]
                plata = restantes[1]
            else:
                oro = restantes[1]
                plata = restantes[0]
        else:
            oro = restantes[0] if len(restantes) > 0 else -1
            plata = -1

        # Mostrar resultados de los incentivos
        for i in range(4):
            if i == id_mejor:
                print(f"Vendedor {i + 1} (${totales_vendedores[i]:.2f}): Viaje al extranjero")
            elif i == id_peor:
                print(f"Vendedor {i + 1} (${totales_vendedores[i]:.2f}): Capacitacion en ventas")
            elif i == oro:
                print(f"Vendedor {i + 1} (${totales_vendedores[i]:.2f}): Tarjeta de regalo (ORO)")
            elif i == plata:
                print(f"Vendedor {i + 1} (${totales_vendedores[i]:.2f}): Tarjeta de regalo (PLATA)")

    elif opcion == 5:
        print("Fin del programa")

