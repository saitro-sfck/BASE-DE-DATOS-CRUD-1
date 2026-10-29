#Escriba una aplicación que calcule el producto de una serie de enteros, los números deben
#almacenarse en un arreglo.
#La aplicación debe solicitar al usuario cuántos números desea ingresar, leerlos desde teclado y
#almacenarlos en el arreglo y mostrar el arreglo.
#Luego debe calcular el producto de todos los enteros contenidos en el arreglo y mostrar el
#resultado.

cantidad = int(input("Ingrese la cantidad de numeros enteros que desea multiplicar:"))
numeros=[0] * cantidad
for i in range(cantidad):
    num= int(input(f"El numero {i+1} a multiplicar es:"))
    numeros[i]=num
print(f"\nEl arreglo almacenado es: {numeros}")

producto_total = 1
for elemento in numeros:
    producto_total= producto_total*elemento

print(f"El producto total es: {producto_total}")



