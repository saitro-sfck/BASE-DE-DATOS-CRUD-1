
##1. Dados 3 números enteros, determinar el mayor y el menor de ellos, si los valores coinciden,
##el algoritmo emitirá un mensaje de alerta, advirtiendo la situación, lo cual implica proceder
##de manera inmediata con su rectificación.
##2. Dado un número decimal, convertirlo a binario o a octal.
##3. Dado un vector de N elementos enteros, calcular el promedio de los valores contenidos en
##el arreglo y determinar el valor menor y mayor con su correspondiente posición.
##4. Calcular la matriz transpuesta de la matriz que resulta de multiplicar 2 matrices de orden
##𝑛 𝑥 𝑚 de números enteros.
##5. Salir

opc=int(input("1. Determinar numero mayor y menor de 3 numeros enteros\n2. Convertir un numero decimal a binario u octal\n3. Calcular el valor promedio de un vector y determinar mayor y menor\n4.matriz transpuesta de la matriz que resulta de multiplicar 2 matrices de orden n x m\n5. Salir\nEscoja una opcion:"))
match opc:
    case 1:
        print("Ingrese los numeros a ordenar:")
        num1=int(input("Ingrese el numero 1: "))
        num2=int(input("Ingrese el numero 2: "))
        num3=int(input("Ingrese el numero 3: "))
        mayor=num1
        menor=num1
        if num1==num2 or num2==num3 or num1==num3:
            print ("Los valores estan repetidos, Ingrese los valores de nuevo:")
        if num2> mayor:
            mayor=num2
        if num3>mayor:
            mayor=num3
        if num2<menor:
            menor = num2
        if num3<menor:
            menor = num3
        print("El numero mayor es: ",mayor)
        print("El numero menor es: ",menor)
    case 2:
        while True:
            print("Escoger si transformar numeros decimales a binario u octal")
            print("1. Binario")
            print("2. Octal")
            opcion = int(input("Ingrese la opcion: "))
            match opcion:
                case 1:
                    numerodec = int(input("Ingrese el número decimal entero: "))

                    # Inicializamos las variables para el cálculo
                    aux = numerodec
                    resultadobin = 0
                    factor = 1

                    # Ciclo de divisiones sucesivas mientras el número sea mayor a 0
                    while aux > 0:
                        residuo = aux % 2  # 1. Tomas el residuo actual (0 o 1)
                        resultadobin = resultadobin + (residuo * factor)  # 2. Lo acumulas en su posición
                        factor = factor * 10  # 3. Avanzas el factor (1, 10, 100, 1000...)
                        aux = aux // 2  # 4. Reduces el número con división entera

                    print(f"El número {numerodec} en binario es: {resultadobin}")
                    break  # Esto rompe el "while True" del menú secundario para volver al menú principal
    case 3:
        n=int(input("Ingrese la cantidad de personas a las que se les tomo la temperatura: "))
        temperaturas = [0.0]*n
        suma_temperatura=0
        for i in range(n):
            temp= float(input(f"Ingrese la temperatura{i+1}: "))
            temperaturas[i] = temp
            suma_temperatura = suma_temperatura + temp

            media= suma_temperatura/n
            contador_superiores= 0
            for i in range (n):
                if temperaturas[i] > media:
                    contador_superiores = contador_superiores + 1
                print("La temperatura media es: ", media)
                print("La temperatura superior a la media es: ", contador_superiores)





































