
ventas_mes= [
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0]
]
vendedor= 00
producto= 00
num_reporte= int(input("Ingrese el numero de reportes:"))
for i in range(num_reporte):
    (print("Reporte numero "+ str(i+1)))

    vendedor_valido=0
    while vendedor_valido == 0:
        vendedor= int(input("Ingrese el numero de vendedor:"))
        if vendedor>=1 or vendedor<=4:
            vendedor_valido=1
        else:
            print("El numero de vendedor es invalido")

    producto_valido=0
    while producto_valido == 0:
        producto= int(input("Ingrese el numero de producto:"))
        if producto>=1 or producto<=5:
            producto_valido=1
        else:
            print("El numero de producto es invalido")
    valor_ventas= float(input("Ingrese el valor de venta:"))
    fila=vendedor-1
    columna= producto-1
    ventas_mes[fila][columna]= ventas_mes[fila][columna]+ valor_ventas

opcion=0
while opcion!=5:
    print("1. Conocer el numero de ventas realizadas por cada vendedor:")
    print("2, Conocer las ventas comercializadas por cada producto:")
    print("3, Conocer las ventas totales del mes pasado:")
    print("4. Mejor vendedor acreedor de un viaje al extranjero:")
    opcion = int(input("Ingrese el numero de opcion:"))

    if opcion == 1:
        # Calcular y mostrar total de cada vendedor
        for i in range(4):
            suma = 0.0
            for j in range(5):
                suma = suma + ventas_mes[i][j]
            print("Vendedor " + str(i + 1) + ": $" + str(suma))

    elif opcion == 2:
        # Calcular y mostrar total de cada producto
        for j in range(5):
            suma = 0.0
            for i in range(4):
                suma = suma + ventas_mes[i][j]
            print("Producto " + str(j + 1) + ": $" + str(suma))

    elif opcion == 3:
        # Calcular y mostrar ventas totales del mes
        total_general = 0.0
        for i in range(4):
            for j in range(5):
                total_general = total_general + ventas_mes[i][j]
        print("Total general vendido: $" + str(total_general))

    elif opcion == 4:
        # Calcular los totales acumulados por vendedor en un vector
        totales = [0.0, 0.0, 0.0, 0.0]
        for i in range(4):
            suma_v = 0.0
            for j in range(5):
                suma_v = suma_v + ventas_mes[i][j]
            totales[i] = suma_v

        # Buscar el mejor y el peor vendedor
        v_mejor = 1
        v_peor = 1
        for i in range(4):
            if totales[i] > totales[v_mejor - 1]:
                v_mejor = i + 1
            if totales[i] < totales[v_peor - 1]:
                v_peor = i + 1

        # Encontrar de forma simple los otros dos vendedores restantes
        otro1 = 0
        otro2 = 0
        for i in range(1, 5):
            if i != v_mejor and i != v_peor:
                if otro1 == 0:
                    otro1 = i
                else:
                    otro2 = i

        # Comparar los restantes para ver quien se lleva Oro y quien Plata
        if totales[otro1 - 1] >= totales[otro2 - 1]:
            oro = otro1
            plata = otro2
        else:
            oro = otro2
            plata = otro1

        # Mostrar los premios asignados
        print("Vendedor " + str(v_mejor) + ": Viaje al extranjero (Mejor)")
        print("Vendedor " + str(v_peor) + ": Capacitacion en ventas (Menor)")
        print("Vendedor " + str(oro) + ": Tarjeta de regalo ORO")
        print("Vendedor " + str(plata) + ": Tarjeta de regalo PLATA")

    elif opcion == 5:
        print("Fin del programa")

















