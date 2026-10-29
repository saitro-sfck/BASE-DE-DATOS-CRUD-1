# Mostrar el catálogo de artículos disponibles y sus precios
print("                  CATÁLOGO DE ARTPICULOS DISPONIBLES                  ")
print("Articulo 1:  $239.99")
print("Articulo 2:  $129.75")
print("Articulo 3:  $99.95")
print("Articulo 4:  $350.89")

# Solicitar al usuario que ingrese los artículos vendidos durante la semana
print("Por favor, Ingresar la cantidad vendida de cada articulo")
artsv1 = float(input("Cantidad vendida de articulos 1: "))
artsv2 = float(input("Cantidad vendida de articulos 2: "))
artsv3 = float(input("Cantidad vendida de articulos 3: "))
artsv4 = float(input("Cantidad vendida de articulos 4: "))

# Evaluamos las variables que ingresó el usuario
if artsv1 >= 0 and artsv2 >= 0 and artsv3 >= 0 and artsv4 >= 0:
    precioart1 = 239.99
    precioart2 = 129.75
    precioart3 = 99.95
    precioart4 = 350.89

    # Calcular el total de ventas brutas sumando el valor de cada artículo vendido
    total_ventas = (precioart1 * artsv1) + (precioart2 * artsv2) + (precioart3 * artsv3) + (precioart4 * artsv4)
    total_ventas = round(total_ventas, 2)

    # Calcular la comisión correspondiente al 9% de las ventas brutas.
    comision = (total_ventas * 0.09)
    comision = round(comision, 2)

    # Calcular el ingreso total del vendedor mediante la fórmula:
    Ingreso_total = 200 + comision
    Ingreso_total = round(Ingreso_total, 2)  # Corregido para que coincida la mayúscula 'Ingreso_total'

    # Mostrar en pantalla:
    print("El total de ventas brutas es:", total_ventas)
    print("El total de comision es:", comision)
    print("El salario base semanal es 200.00")
    print("El Ingreso total del vendedor es:", Ingreso_total)
else:
    print("\n[Error]: No se permiten cantidades negativas de articulos vendidos ")
