opc = int(input("1.Ecuación de primer grado (ax + b = 0)\n2.Cálculo de distancia y combustible consumido\n3. Sistema de pedidos Pizzería M\nSeleccione la opcion ha ejecutar: "))
match opc:
    case 1:
        # 1. Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = c ) y
        # escriba la solución. Se recuerda que una ecuación de primer grado puede no tener solución,
        # tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de
        # las soluciones es x = -b / a
        print("1. Resolver ecuaciones de primer grado")
        a= float(input("Ingrese el valor de a: "))
        b= float(input("Ingrese el valor de b: "))
        c= float(input("Ingrese el valor de c: "))
        if a!=0:
            x= (c-b)/a
            print ("La ecuacion tiene una unica solucion, el valor de x es: ",x)
        else:
            print ("No hay solucion")
        if b==c:
            print ("Infinitas soluciones")
    case 2:
        # 2. Cree un programa que lea una distancia recorrida en kilómetros. Según la distancia, determine cuántos
        # kilómetros se recorrieron en terreno llano, pedregoso y montañoso, y calcule el combustible consumido:
        # • Llano: 5 litros cada 100 km (hasta 80 km)
        # • Pedregoso: 10 litros cada 100 km (de 81 a 170 km)
        # • Montañoso: 12 litros cada 100 km (más de 170 km)
        print("2. Calcular combustible consumido en base a los km recorridos")
        distancia= float(input("Ingrese el valor de la distancia en km"))
        if distancia <= 80:
            llano=distancia
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
        print(" --- SISTEMA DE PEDIDOS: PIZZERIA ___")
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
                print(f"\n[Menú {categoria_pizza}]")
                print("Base incluida: Mozzarella y Tomate.")
                print("1. Tofu\n2. Pimiento")
                item_adicional = int(input("Seleccione el ingrediente extra que desea añadir: "))

                if item_adicional == 1:
                    componentes_base.append("Tofu")
                elif item_adicional == 2:
                    componentes_base.append("Pimiento")
                unidades_pedidas = int(input("\n¿Cuántas unidades de pizza desea solicitar? "))
                monto_subtotal = unidades_pedidas * costo_unidad

                if unidades_pedidas < 5:
                    tasa_descuento = 12
                else:
                    tasa_descuento = 20
            case 2:
                categoria_pizza = "No vegetariana"
                costo_unidad=13
                print(f"\n[Menú {categoria_pizza}]")
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

                if unidades_pedidas < 5:
                    tasa_descuento = 10
                else:
                    tasa_descuento = 15

        dinero_descuento = monto_subtotal * (tasa_descuento / 100)
        neto_pagar = monto_subtotal - dinero_descuento

        print("\n================ DETALLE DE LA ORDEN ================")
        print(f"- Tipo de pizza elegido: {categoria_pizza}")
        print(f"- Los ingredientes de la pizza: {', '.join(componentes_base)}")
        print(f"- La cantidad de pizzas solicitadas:",unidades_pedidas)
        print(f"- Precio unitario: ${costo_unidad}")
        print(f"- Subtotal de la compra: ${monto_subtotal}")
        print(f"- Porcentaje de descuento aplicado: {tasa_descuento}%")
        print(f"- Valor del descuento: ${dinero_descuento:.2f}")
        print(f"- El total a pagar: ${neto_pagar:.2f}")

    case _:
        print("[ERROR]: Opción fuera de rango. Ingrese un valor válido (1-3).")




























