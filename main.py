numeros = []

while True:
    dato = input("Ingresa un número (o escribe 'salir'): ")

    if dato.lower() == "salir":
        break

    try:
        numero = int(dato)
        numeros.append(numero)
    except:
        print("⚠️ Debes ingresar un número válido")

if len(numeros) > 0:
    print(f"\nNúmeros ingresados: {numeros}")
    print(f"Cantidad: {len(numeros)}")
    print(f"Promedio: {sum(numeros) / len(numeros)}")
else:
    print("No ingresaste números")