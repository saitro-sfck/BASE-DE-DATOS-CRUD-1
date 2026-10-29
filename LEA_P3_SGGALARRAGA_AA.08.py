
opc = int(input("1.Ecuación de primer grado ax + b = c\n2.Cálculo de distancia y combustible consumido\n3. Sistema de pedidos Pizzería GG\nSeleccione la opcion ha ejecutar: "))
match opc:
    case 1:
        # 1. Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = c ) y
        # escriba la solución. Se recuerda que una ecuación de primer grado puede no tener solución,
        # tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de
        # las soluciones es x = -b / a
        print("1. Resolver ecuaciones de primer grado")
        a = float(input("Ingrese el valor de a"))
        b = float(input("Ingrese el valor de b"))
        c = float(input("Ingrese el valor de c"))
        if a != 0:
            x = (c - b) / a
            print("La ecuacion tiene una unica solucion, el valor de x es: ", x)
        else:
            print("No hay solucion")
        if b == c:
            print("Infinitas soluciones")

    case 2:
        # 2. Cree un programa que lea una distancia recorrida en kilómetros. Según la distancia, determine cuántos
        # kilómetros se recorrieron en terreno llano, pedregoso y montañoso, y calcule el combustible consumido:
        # • Llano: 5 litros cada 100 km (hasta 80 km)
        # • Pedregoso: 10 litros cada 100 km (de 81 a 170 km)
        # • Montañoso: 12 litros cada 100 km (más de 170 km)
        print("2. Calcular combustible consumido en base a los km recorridos")
        distancia = float(input("Ingrese el valor de la distancia en km"))
        if distancia <= 80:
            llano = distancia
            pedr = 0
            mont = 0
        else:
            if distancia <= 170:
                llano = 80
                pedr = distancia - 80
                mont = 0
            else:
                llano = 80
                pedr = 90
                mont = distancia - 170

        Comb_llano = llano * (5 / 100)
        Comb_pedr = pedr * (10 / 100)
        Comb_mont = mont * (12 / 100)
        Totalcomb = Comb_llano + Comb_mont + Comb_pedr

        print("los kilómetros en terreno llano son :", llano)
        print("Los kilómetros en terreno pedregoso son:", pedr)
        print("Los Kilómetros en terreno montañoso son:", mont)
        print("El combustible en terreno llano es:", Comb_llano, "litros")
        print("El combustible en terreno pedregoso es:", Comb_pedr, "litros")
        print("El combustible en terreno montañoso es:", Comb_mont, "litros")
        print("El combustible total es:", Totalcomb, "litros")

    case 3:
        # 3. Una pizzería ofrece pizzas a sus clientes. Los ingredientes disponibles para cada tipo de
        # pizza son los siguientes:
        # Ingredientes vegetarianos:
        # • Pimiento
        # • Tofu
        # Ingredientes no vegetarianos:
        # • Pepperoni
        # • Jamón
        # • Tocino
        # Todas las pizzas incluyen mozzarella y tomate como ingredientes base.
        # Los precios son:
        # • Pizza vegetariana: $16
        # • Pizza no vegetariana: $13
        # Los descuentos a calcular son:
        # Pizzas vegetarianas
        # • Si se solicitan menos de 5 pizzas, se aplica un descuento del 12% sobre el subtotal.
        # • Si se solicitan más de 5 pizzas, se aplica un descuento del 20% sobre el subtotal.
        # Pizzas no vegetarianas
        # • Si se solicitan menos de 5 pizzas, se aplica un descuento del 10% sobre el subtotal.
        # • Si se solicitan más de 5 pizzas, se aplica un descuento del 15% sobre el subtotal.
        # Escriba un programa que:
        # • Pregunte al usuario si desea una pizza vegetariana o no vegetariana.
        # • Muestre el menú de ingredientes disponibles según el tipo de pizza seleccionado.
        # • Permita elegir un solo ingrediente adicional.
        # • Pregunte cuántas pizzas desea ordenar.
        # • Calcule el subtotal de la compra.
        # • Determine el descuento correspondiente según el tipo de pizza y la cantidad solicitada.
        # • Calcule el valor del descuento y el total a pagar.
        # • Muestre en pantalla:
        # -El tipo de pizza elegido.
        # -Los ingredientes de la pizza (mozzarella, tomate and el ingrediente seleccionado).
        # -La cantidad de pizzas solicitadas.
        # -El precio unitario.
        # -El subtotal de la compra.
        # -El porcentaje de descuento aplicado.
        # -El valor del descuento.
        # - El total a pagar.
        print(" --- SISTEMA DE PEDIDOS: PIZZERIA GG___")
        print("1) Estilo Vegetariana\n2) Estilo No Vegetariana")
        seleccion_usuario = int(input("Por favor, elija una opción: "))
        categoria_pizza = ""
        componentes_base = ["Mozzarella", "Tomate"]
        costo_unidad = 0
        tasa_descuento = 0

        match seleccion_usuario:
            case 1:
                categoria_pizza = "Vegetariana"
                costo_unidad = 16
                print("\n", categoria_pizza)
                print("Base incluida: Mozzarella y Tomate.")
                print("1. Tofu\n2. Pimiento")
                item_adicional = int(input("Seleccione el ingrediente extra que desea añadir: "))

                if item_adicional == 1:
                    componentes_base.append("Tofu")
                elif item_adicional == 2:
                    componentes_base.append("Pimiento")
                unidades_pedidas = int(input("\n¿Cuántas unidades de pizza desea solicitar? "))
                monto_subtotal = unidades_pedidas * costo_unidad

                if unidades_pedidas <= 5:
                    tasa_descuento = 12
                else:
                    tasa_descuento = 20
            case 2:
                categoria_pizza = "No vegetariana"
                costo_unidad = 13
                print("\n[Menú]", categoria_pizza)
                print("Base incluida: Mozzarella y Tomate.")
                print("1. Pepperoni\n2. Tocino\n3. Jamón")
                item_adicional = int(input("Seleccione el ingrediente extra que desea añadir: "))

                if item_adicional == 1:
                    componentes_base.append("Pepperoni")
                elif item_adicional == 2:
                    componentes_base.append("Tocino")
                elif item_adicional == 3:
                    componentes_base.append("Jamon")

                unidades_pedidas = int(input("\n¿Cuántas unidades de pizza desea solicitar? "))
                monto_subtotal = unidades_pedidas * costo_unidad

                if unidades_pedidas <= 5:
                    tasa_descuento = 10
                else:
                    tasa_descuento = 15

        dinero_descuento = monto_subtotal * (tasa_descuento / 100)
        neto_pagar = monto_subtotal - dinero_descuento

        print("\n================ DETALLE DE LA ORDEN ================")
        print("- Tipo de pizza elegido:", categoria_pizza)
        print("- Los ingredientes de la pizza:", ", ".join(componentes_base))
        print("- La cantidad de pizzas solicitadas:", unidades_pedidas)
        print("- Precio unitario: $", costo_unidad)
        print("- Subtotal de la compra: $", monto_subtotal)
        print("- Porcentaje de descuento aplicado:", tasa_descuento, "%")
        print("- Valor del descuento: $", dinero_descuento)
        print("- El total a pagar: $", neto_pagar)

    case _:
        print("[ERROR]: Opción fuera de rango. Ingrese un valor válido (1-3).")
















        while(continuar):
        print("      SISTEMA DE ORDEN EN FUNCION AL SUELDO DE LOS EMPLEADOS       ")
        print("1. conocer el mayor sueldo de un empleado ")
        print("2. Salir")
        opc= "Ingrese la accion que desea realizar:"
        if opc == "2"
            print("Saliendo del programa...")
            (continuar): False
        elif opc == "1":
        n= int(input("Ingrese el numero de empleados de la empresa"))
        sueldo_mayor= 0
        ordenbestempleadoUwU= 0
        for i in range (n):
            print(f"\nDatos del empleado {i+1}:")
            numorden= int(input("Ingrese el numero de orden:"))
            sueldo= float(input("Ingrese el sueldo:"))

        if sueldo > sueldo_mayor:
            sueldo_mayor= sueldo
            ordenbestempleadoUwU = numorden
        print("\n========================================")
        print(f"El empleado con el mayor sueldo es el número de orden: {ordenbestempleadoUwU}")
        print(f"Su sueldo es de: ${sueldo_mayor:.2f}")
        print("========================================")