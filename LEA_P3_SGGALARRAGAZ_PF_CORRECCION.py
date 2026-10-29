#Una compañía paga a sus vendedores una comisión por las ventas realizadas semanalmente. Cada vendedor
#recibe un salario base de $200 más el 9% de sus ventas totales de la semana. La empresa realiza las
#transferencias bancarias utilizando únicamente valores enteros; por lo tanto, cuando el salario calculado
#contiene decimales, la parte decimal debe descartarse. Construya un programa de computadora en Python
#que permita registrar las ventas semanales del conjunto de vendedores de acuerdo a los siguientes
#requerimientos:
#1. Calcular el desglose de la nómina total del personal de ventas.
#Vendedor:
#salario base:
#ventas totales:
#comisión:
#salario total:

#2. Determinar el vendedor que recibió el salario más alto y mostrar su salario.
#3. Determinar el vendedor que recibió el salario más bajo y mostrar su salario.
#4. Calcular la cantidad de vendedores por rango salarial

num_vendedores = int(input("Ingrese la cantidad de vendedores: "))

nombres = [0] * num_vendedores
ventas = [0] * num_vendedores

for i in range(num_vendedores):
    nombres[i] = input("Nombre o código del vendedor: ")
    ventas[i] = float(input("Ingrese las ventas totales en dólares: "))

salarios_base = [0] * num_vendedores
comisiones = [0] * num_vendedores
salarios_totales = [0] * num_vendedores

rangos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(num_vendedores):
    base = 200
    comision = ventas[i] * 0.09
    total = int(base + comision)

    salarios_base[i] = base
    comisiones[i] = comision
    salarios_totales[i] = total

    if total >= 200 and total <= 299:
        rangos[0] = rangos[0] + 1
    elif total >= 300 and total <= 399:
        rangos[1] = rangos[1] + 1
    elif total >= 400 and total <= 499:
        rangos[2] = rangos[2] + 1
    elif total >= 500 and total <= 599:
        rangos[3] = rangos[3] + 1
    elif total >= 600 and total <= 699:
        rangos[4] = rangos[4] + 1
    elif total >= 700 and total <= 799:
        rangos[5] = rangos[5] + 1
    elif total >= 800 and total <= 899:
        rangos[6] = rangos[6] + 1
    elif total >= 900 and total <= 999:
        rangos[7] = rangos[7] + 1
    elif total >= 1000:
        rangos[8] = rangos[8] + 1

print("\n1 DESGLOSE DE LA NOMINA")
for i in range(num_vendedores):
    print("Vendedor:", nombres[i])
    print("salario base:""$",salarios_base[i])
    print("ventas totales:""$",ventas[i])
    print("comision:""$",comisiones[i])
    print("salario total:""$", salarios_totales[i])

pos_max = 0
pos_min = 0

for i in range(1, num_vendedores):
    if salarios_totales[i] > salarios_totales[pos_max]:
        pos_max = i
    if salarios_totales[i] < salarios_totales[pos_min]:
        pos_min = i

print("\n2 SALARIO MAS ALTO")
print("Vendedor:", nombres[pos_max])
print("Salario:""$", salarios_totales[pos_max])

print("\n3 SALARIO MAS BAJO")
print("Vendedor:", nombres[pos_min])
print("Salario:""$", salarios_totales[pos_min])

etiquetas = [
    "$200-299",
    "$300-399",
    "$400-499",
    "$500-599",
    "$600-699",
    "$700-799",
    "$800-899",
    "$900-999",
    "$1000 en adelante"
]

print("\n4 RANGOS SALARIALES")
for i in range(9):
    print(etiquetas[i], ":", rangos[i])
