ventas = [
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]
]

continuar = 1

while continuar == 1:
    vendedor = int(input("Ingrese el numero de vendedor (1 a 4): "))
    producto = int(input("Ingrese el numero de producto (1 a 5): "))
    monto = float(input("Ingrese el valor total vendido: "))

    if vendedor >= 1 and vendedor <= 4 and producto >= 1 and producto <= 5:
        ventas[producto - 1][vendedor - 1] = ventas[producto - 1][vendedor - 1] + monto
    else:
        print("Datos incorrectos. Intente de nuevo.")

    continuar = int(input("Desea ingresar otra nota de venta? (1: Si / 0: No): "))

print("")
print("Producto         V1       V2       V3       V4   Total Producto")
print("----------------------------------------------------------------")

totales_vendedores = [0.0, 0.0, 0.0, 0.0]

for i in range(5):
    total_fila = 0.0
    num_producto = i + 1
    texto_fila = f"Prod {num_producto} "

    for j in range(4):
        valor = ventas[i][j]
        texto_fila = texto_fila + f"{valor:>8} "
        total_fila = total_fila + valor
        totales_vendedores[j] = totales_vendedores[j] + valor

    texto_fila = texto_fila + f"{total_fila:>16}"
    print(texto_fila)

print("----------------------------------------------------------------")

texto_totales = "Total Vend."
total_general = 0.0

for j in range(4):
    valor_vendedor = totales_vendedores[j]
    texto_totales = texto_totales + f"{valor_vendedor:>8} "
    total_general = total_general + totales_vendedores[j]

texto_totales = texto_totales + f"{total_general:>16}"
print(texto_totales)

