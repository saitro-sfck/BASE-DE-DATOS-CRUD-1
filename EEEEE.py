ventas_mes=[
    [0.0,0.0,0.0,0.0,0.0], #Vendedor 1
    [0.0,0.0,0.0,0.0,0.0],  #Vendedor 2
    [0.0,0.0,0.0,0.0,0.0],  #Vendedor 3
    [0.0,0.0,0.0,0.0,0.0]  #Vendedor 4
]
vendedor= 0
producto= 0
num_reportes= int(input("Ingrese el numero de reportes:"))
for i in range (num_reportes):
    print("reporte" + str(i + 1))

    vendedor_valido= 0
    while vendedor_valido==0:
        vendedor= int(input("Ingrese el numero de vendedor:"))
        if vendedor>=1 or vendedor<=4:
            vendedor_valido=1
        else:
            print("El numero de vendedor es invalido")
    producto_valido= 0
    while producto_valido==0:
        producto= int(input("Ingrese el numero de producto:"))
        if producto>=1 or producto<=4:
            producto_valido=1
        else:
            print("El numero de producto es invalido")

    valor_ventas= float(input("Ingrese el valor de la venta:"))
    fila = vendedor-1
    columna= producto-1
    ventas_mes[fila][columna]= ventas_mes[fila][columna]+ valor_ventas
opcion=0
while opcion != 5:
    print("1. Conocer las ventas totales realizadas por cada vendedor:")
    print("2. Conocer las ventas comercializadas por cada producto:")
    print("3. Conocer las ventas totales del mes pasado:")
    print("4. Conocer quien fue el vendedor ganador de un viaje al extranjero:")
    print("5. PODIO DE VENDEDORES:")
    print("6. Vendedor que necesita capacitacion:")
    opcion= int(input("Ingrese la opcion que desee:"))
    if opcion==1:
        for i in range(4):
            suma= 0.0
            for j in range(5):
                suma= suma + ventas_mes[i][j]
            print("Vendedor " + str(i+1) + ": " +str(suma))
    elif opcion==2:
        for j in range(5):
            suma= 0.0
            for i in range(4):
                suma= suma + ventas_mes[i][j]
            print("Producto " + str(j+1) + ": " + str(suma))
    elif opcion==3:
        valor_total= 0
        for i in range(4):
            for j in range(5):
                valor_total = valor_total + ventas_mes[i][j]
            print("Las ventas del mes pasado fueron: " + str(valor_total))
    elif opcion==4:
        totales=[0.0,0.0,0.0,0.0]
        for i in range(4):
            suma_v= 0.0
            for j in range(5):
                suma_v= suma_v+ ventas_mes[i][j]
            totales[i]= suma_v
    v_mejor= 1
    v_peor= 1
    for i in range (4):
        if totales[i]>totales[v_mejor-1]:
            v_mejor= i+1
    for j in range (5):
        if totales[i]<totales[v_peor-1]:
            v_peor= i+1

    otro1= 0
    otro2= 0
















