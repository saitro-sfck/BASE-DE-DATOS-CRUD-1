#El Clasificador de Números (Fácil):
#Escribe un programa que pida al usuario un número entero.
# #El programa debe imprimir si el número es "Positivo y Par", "Positivo e Impar",
# "Negativo" o "Cero".

#Calculadora de Descuentos Múltiples (Medio):
#Una tienda ofrece descuentos según el monto de la compra y si el cliente tiene una membresía.

#Si la compra es menor a $50: no hay descuento.

#Si está entre $50 y $100: 5% de descuento.

##Si es mayor a $100: 10% de descuento.

#Condición extra: Si el cliente tiene membresía (un valor booleano o True/False),
# se le aplica un 5% de descuento adicional sobre el total ya descontado.
#Pide el monto y si tiene membresía, e imprime el total final a pagar.

#El Triángulo Válido (Desafío):
#Pide al usuario tres longitudes (a, b, c). Primero, determina si pueden formar un
# triángulo (la suma de dos lados siempre debe ser mayor al tercero). Si es válido,
# clasifícalo en Equilátero (3 lados iguales), Isósceles (2 iguales) o Escaleno (todos diferentes).
opc=int(input(" 1. CLASIFICADOR DE NUMEROS  \n 2. CALCULADORA DE DESCUENTOS MULTIPLES \n Selecciona la opcion a ejecutar: "))
match opc:
    case 1:
        print("1. CLASIFICADOR DE NUMEROS")
        numero_dusuario = int(
            input("Ingrese el numero entero a conoceer si es positivo, par, impar, negativo o cero: "))
        if numero_dusuario > 0:
            print("El numero es positivo")
        if numero_dusuario < 0:
            print("El numero es negativo")
        if numero_dusuario == 0:
            print("El numero es cero")
        if numero_dusuario % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    case 2:
        print("2. CALCULADORA DE DESCUENTOS multiples")
        valord_compra = float(input("Ingrese el valor de compra: "))

        # Recuerda cambiar este segundo 'if' por un 'elif' para que no choque con el de arriba
        if 50 <= valord_compra <= 100:
            valord_descuento = valord_compra * 0.05
            valor_casitotal = valord_compra - valord_descuento
            print("El valor de compra es: ", valor_casitotal)
        elif valord_compra > 100:
            valord_descuento = valord_compra * 0.1
            valor_casitotal = valord_compra - valord_descuento  # Añade esta línea para que funcione con > 100
            print("El valor de compra es: ", valor_casitotal)
        else:
            valor_casitotal = valord_compra
            print("El valor de compra es: ", valord_compra)

        tiene_membresia = int(input("Ingrese el numero 1 si tiene membresia o el numero 0 si no la tiene: "))

        if tiene_membresia == 0:
            booleano_membresia = False
        elif tiene_membresia == 1:
            booleano_membresia = True
        else:
            booleano_membresia = False
        if booleano_membresia:
            valor_total = valor_casitotal - (valor_casitotal * 0.05)
        else:
            valor_total = valor_casitotal
        print("El valor total es: ", valor_total)
    






