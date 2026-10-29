ventas_mes= [
[0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0]
]
vendedor=0
producto=0
num_reporte= int(input("Ingrese el numero de reporte: "))
for i in range(num_reporte):
    print("Reporte numero " + str(i+1))

    vendedor_valido=0
    while vendedor_valido==0:
        vendedor=int(input("Ingrese el numero de vendedor: "))
        if vendedor>=1 or vendedor<=4:
            vendedor_valido=1
    producto_valido=0
    while producto_valido==0:
        producto= int(input("Ingrese el numero de producto: "))
        if producto>=1 or producto<=5:
            producto_valido=1
    valor_ventas= float(input("Ingrese el valor de la venta: "))
    fila= vendedor-1
    columna= producto-1
    ventas_mes[fila][columna]= ventas_mes[fila][columna]+ valor_ventas
opcion=0
while opcion!=5:
    print("1. Conocer el numero de ventas realizadas por cada vendedor:")
    print("2, Conocer las ventas comercializadas por cada producto:")
    print("3, Conocer las ventas totales del mes pasado:")
    print("4. Mejor vendedor acreedor de un viaje al extranjero:")
    opcion=int(input("Ingrese el numero de opcion: "))

    if opcion==1:
        for i in range(4):
            suma=0
            for j in range(5):
                suma= suma + ventas_mes[i][j]
            print("vendedor: " + str(i+1) + ": " + str(suma))
    if opcion==2:
        for j in range(5):
            suma=0
            for i in range(4):
                suma= suma + ventas_mes[i][j]
            print("producto " + str(j+1) + ": " + str(suma))
    if opcion==3:
        ventas_totales=0
        for i in range(4):
            for j in range(5):
                ventas_totales= ventas_totales + ventas_mes[i][j]
    if opcion==4:
        totales=[0.0,0.0,0.0,0.0]
        for i in range(4):
            suma_v= 0
            for j in range(5):
                suma_v= suma_v + ventas_mes[i][j]
            totales[i]=suma_v
        v_mejor=1
        v_peor=1
        for i in range(1,5):
            if totales[i]>totales[v_mejor-1]:
                v_mejor=i+1
            if totales[1]<totales[v_peor-1]:
                v_peor=i+1
        otro1=0
        otro2=0
        for i in range(1,5):
            if i!=v_mejor and i!=v_peor:
                if otro1==0:
                    otro1 = i
            else:
                otro2 = i
            if totales[otro1 - 1] >= totales[otro2 - 1]:
                oro = otro1
                plata = otro2
            else:
                oro = otro2
                plata = otro1

            print("vendedor" + str(v_mejor) + "Viaje al extranjero")
            print("vendedor" + str(v_peor) + "capacitacion de ventas")
            print("venddor" + str(otro1) + "oro")
            print("venddor" + str(otro2) + "plata")



















